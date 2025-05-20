from django.db import models
from django.utils import timezone
from datetime import timedelta



class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    def published_recently(self):
        return self.published_date >= timezone.now() - timedelta(days=7)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author_name} on {self.post.title}'



    