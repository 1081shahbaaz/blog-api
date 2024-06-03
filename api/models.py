from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Common(models.Model):
    created_at = models.TimeField(auto_now=False, auto_now_add=True)
    updated_at = models.TimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        
class Category(Common):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Post(Common):
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField()
    Category = models.ManyToManyField(Category)
    image = models.FileField(null=True,blank=True)
    
    def __str__(self):
        return self.title

class Comment(Common):
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=2)
    
    def __str__(self) -> str:
        return f'{self.body[:20]}....'
