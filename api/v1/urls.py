from django.urls import path, include
from api.v1.docs import doc_urlpatterns
from .views.post import ListPostAPIView, CreatePostAPIView, DetailPostAPIView
from .views.account import UserCreateAPIView, UserListAPIView, UserDetailAPIView
from .views.comment import ListCommentAPIView, DetailCommentAPIView, CreateCommentAPIView
from .views.category import ListCategoryAPIView, CreateCategoryAPIView

app_name = 'api'

urlpatterns = [
   path('', include(doc_urlpatterns)),

   path("post/", ListPostAPIView.as_view(), name="list_post"),
   path("post/create/", CreatePostAPIView.as_view(), name="create_post"),
   path("post/<str:slug>/", DetailPostAPIView.as_view(), name="post_detail"),
   path("post/<str:slug>/comment/", ListCommentAPIView.as_view(), name="list_comment"),
   path(
      "post/<str:slug>/comment/create/",
      CreateCommentAPIView.as_view(),
      name="create_comment",
   ),
   path(
      "post/<str:slug>/comment/<int:id>/",
      DetailCommentAPIView.as_view(),
      name="comment_detail",
   ),

   path('category/<str:slug>', ListCategoryAPIView.as_view(), name="category_list"),
   path('category/create/', CreateCategoryAPIView.as_view(), name="create_category"),

   path("user/", UserListAPIView.as_view(), name="user_detail"),
   path("user/register/", UserCreateAPIView.as_view(), name="user_create"),
   path("user/<str:id>/", UserDetailAPIView.as_view(), name="user_detail"),
]