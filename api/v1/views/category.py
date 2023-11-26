from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from api.v1.pagination import PostLimitOffsetPagination
from blog.models import Post

from api.v1.serializers.posts import PostListSerializer
from api.v1.serializers.category import CategoryCreateUpdateSerializer
from blog.models import Category, Post


class CreateCategoryAPIView(APIView):
    """
    post:
        Returns a list of posts in a specific category

        parameters: [parent ,title ,slug ,status ,position]
    """

    queryset = Post.objects.all()
    serializer_class = CategoryCreateUpdateSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        print(request.__dir__())
        print(kwargs)
        print(request.data)
        serializer = CategoryCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)
        

class ListCategoryAPIView(APIView):
    """
    get:
        Returns a list of posts in a specific category
    """

    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PostLimitOffsetPagination

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        post = Post.objects.filter(category=category)
        serializer = PostListSerializer(post, many=True)
        return Response(serializer.data, status=200)
    

