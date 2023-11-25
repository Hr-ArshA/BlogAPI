from rest_framework import serializers
from blog.models import Category, Post

class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'slug',
            'title',
            'posts',
        ]

    def get_slug(self, obj):
        return obj.slug

    
    def get_posts(self, obj):
            posts = Post.objects.filter(category__id=obj.id)