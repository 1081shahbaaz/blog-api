from rest_framework import serializers
from .models import Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Post
        fields = ('id','title','content','Category', 'comments','image')

    def get_comments(self,obj):
        data = obj.comments.all().values('body','commenter__username')
        return data
