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
from api.v1.permissions import IsAuthorOrReadOnly
from api.v1.serializers.posts import (
    PostCreateUpdateSerializer,
    PostListSerializer,
    PostDetailSerializer,

)