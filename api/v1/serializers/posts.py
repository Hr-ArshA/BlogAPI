import os
from rest_framework import serializers
from blog.models import Post, Comment, Category
from config import settings
from .comment import CommentSerializer
from accounts.models import Profile

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "description",
            "content",
            "cover",
            "author",
            "category",
            "is_special",
            "status"
        ]

    def validate_title(self, value):
        if len(value) > 256:
            return serializers.ValidationError("Max title length is 256 characters")
        return value

    def validate_description(self, value):
        if len(value) > 256:
            return serializers.ValidationError(
                "Max description length is 256 characters"
            )
        return value
    
    def clean_image(self, value):
        initial_path = value.path
        new_path = settings.MEDIA_ROOT + value.name
        os.rename(initial_path, new_path)
        return value


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "url",
            "title",
            "author",
            "cover",
            "category",
            "description",
            "comments",
        ]

    def get_comments(self, obj):
        qs = Comment.objects.filter(parent=obj).count()
        return qs

    def get_url(self, obj):
        return obj.get_api_url()
    

class PostDetailSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Post
        fields = [
            "id",
            "slug",
            "title",
            'category',
            "description",
            "content",
            "author",
            "cover",
            "created",
            "updated",
            "comments",
        ]
    
    

    def get_slug(self, obj):
        return obj.slug

    def get_comments(self, obj):
        qs = Comment.objects.filter(parent=obj)
        try:
            serializer = CommentSerializer(qs, many=True)
        except Exception as e:
            print(e)
        return serializer.data