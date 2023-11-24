from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from api.v1.permissions import IsOwner
from api.v1.serializers.accounts import UserSerializer

# Create your views here.

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    """
    post:
        Create new user instance. Returns username, email of the created user.

        parameters: [username, email, password]
    """

    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class UserListAPIView(ListAPIView):
    """
    get:
        Returns list of all exisiting users
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the detail of a user instance

        parameters: [id]
    
    put:
        Update the detail of a user instance

        parameters: [id, username, email, password]
    
    delete:
        Delete a user instance
        
        parameters: [id]
    """

    permission_classes = [IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'