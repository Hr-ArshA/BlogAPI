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
from api.v1.serializers.category import CategoryCreateUpdateSerializer, CategoryDetailSerializer
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
    

class DetailCategoryAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a post instance. Searches post using slug field.

    put:
        Updates an existing post. Returns updated post data

        parameters: [slug, title, content, description, cover]

    delete:
        Delete an existing post

        parameters = [slug]
    """

    queryset = Category.objects.all()
    lookup_field = "slug"
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]