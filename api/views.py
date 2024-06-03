from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, PostSerializer, CommentSerializer
from .models import Category, Post, Comment
from rest_framework import permissions
from .permissions import IsCommenterOrReadOnly, IsAuthorOrReadOnly
from rest_framework import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class Categories_gen_view(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class Category_gen_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class Posts_gen_view(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class Post_gen_view(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class Comments_gen_view(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(commenter=self.request.user)

class Comment_gen_view(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCommenterOrReadOnly]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer