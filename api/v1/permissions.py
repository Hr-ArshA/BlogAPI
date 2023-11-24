from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """
    Custom permission to check if the user is owner of the object. 
    """
    message = "You can not delete another user"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj == request.user


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        '''
        Authenticated users only can see list view
        '''
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        ''' 
        Read permissions are allowed to any request so we'll always
        allow GET, HEAD, or OPTIONS requests 
        '''
        if request.method in SAFE_METHODS:
            return True
        '''
        Write permissions are only allowed to the author of a post
        '''
        return obj.author == request.user

