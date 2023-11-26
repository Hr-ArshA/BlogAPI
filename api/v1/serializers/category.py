from rest_framework import serializers
from blog.models import Category, Post

class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['parent' ,'title' ,'slug' ,'status' ,'position']
