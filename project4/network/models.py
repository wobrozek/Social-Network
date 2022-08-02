import email
from sqlite3 import Timestamp
from xml.etree.ElementTree import Comment
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class follow(models.Model):
    user=models.ForeignKey("User", on_delete=models.CASCADE,related_name="followers")
    followers=models.ManyToManyField("User",related_name="follower")

#      def serialize(self):
#         return{
#             "id": self.id,
#             "user": self.user,
#             "followers":[user for follow in self.followers.all()]        
#         }
class Post(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE)
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


class Comment(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    post= models.ForeignKey("Post",on_delete=models.CASCADE, related_name="posts")
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
