from django.contrib import admin
from django.urls import path, include
from .views import Categories_gen_view, Category_gen_view, Posts_gen_view, Post_gen_view, Comments_gen_view, Comment_gen_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('blogs/categories/', Categories_gen_view.as_view()),
    path('blogs/category/<int:pk>/', Category_gen_view.as_view()),
    path('blogs/posts/', Posts_gen_view.as_view()),
    path('blogs/post/<int:pk>/', Post_gen_view.as_view()),
    path('blogs/posts/comments', Comments_gen_view.as_view()),
    path('blogs/posts/comment/<int:pk>', Comment_gen_view.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]