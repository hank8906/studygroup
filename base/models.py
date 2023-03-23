from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 定義Topic的Ｍodel
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
      return self.name

# 定義Room的Ｍodel
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null = True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null = True)
    name = models.CharField(max_length=200)
    # null=True : sets NULL (versus NOT NULL) on the column in DB
    # blank=True : field types such as DateTimeField,ForeignKey will be stored as NULL in DB.
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
      ordering = ['-updated','-created']

    def __str__(self):
      return self.name

# 定義Message的Ｍodel
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(default='')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.body[0:50]
