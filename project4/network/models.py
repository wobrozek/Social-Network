import email
from sqlite3 import Timestamp
from xml.etree.ElementTree import Comment
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post():
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="author")
    body = models.CharField(max_length=64)
    likes = models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return{
            "id": self.id,
            "author": self.author,
            "body": self.body,
            "likes": self.likes,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")           
        }


class Comment():
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="author")
    post= models.ForeignKey("Post",on_delete=models.CASCADE, related_name="author")
    body = models.CharField(max_length=64)
    likes = models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return{
            "id": self.id,
            "post":self.post,
            "author": self.author,
            "body": self.body,
            "likes": self.likes,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")           
        }
