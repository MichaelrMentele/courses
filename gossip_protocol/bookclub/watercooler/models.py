from django.db import models


class Gossip(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Member(models.Model):
    port = models.IntegerField()
    favorite_book = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
