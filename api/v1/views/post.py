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

from extentions.ip_utils import get_client_ip
from api.v1.pagination import PostLimitOffsetPagination
from blog.models import Post, PostViews
from accounts.models import IPAddress
from api.v1.permissions import IsAuthorOrReadOnly
from api.v1.serializers.posts import (
    PostCreateUpdateSerializer,
    PostListSerializer,
    PostDetailSerializer,
)

from accounts.models import Profile
from redis import Redis
import json

# Create your views here.
class CreatePostAPIView(APIView):
    """
    post:
        Creates a new post instance. Returns created post data

        parameters: [title, slug, description, content, cover, category, is_special, status]
    """

    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = PostCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = Profile.objects.get(user__id=request.user.id)
            serializer.save(author=user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class ListPostAPIView(ListAPIView):
    """
    get:
        Returns a list of all existing posts
    """

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PostLimitOffsetPagination


class DetailPostAPIView(RetrieveUpdateDestroyAPIView):
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

    # queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostDetailSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        this_redis = Redis(host='redis', port=6379, password='testpass123', decode_responses=True)

        queryset = Post.objects.get(slug=kwargs['slug'])

        address = get_client_ip(request)
        # print(address, type(address))

        new_seen = json.dumps({'slug': kwargs['slug'], 'ip': address})
        this_redis.lpush('new_seen', new_seen)

        c = this_redis.lrange('new_seen', 0, -1)
        this_redis.rpop('new_seen')
        print(c)
        # ip = IPAddress.objects.create(ip_address=address)
        # PostViews.objects.create(article=queryset, ip_address=ip).save()
        # ip.save()
        
        serializer = PostDetailSerializer(queryset)
        return Response(serializer.data, status=200)

