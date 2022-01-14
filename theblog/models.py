from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime , date

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse("home")

class Post(models.Model):
    tittle = models.CharField(max_length=255)
    tittle_tag = models.CharField(max_length=255)
    category = models.CharField(max_length=255 , default='coding')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tittle + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse("home")
    

class Comment(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment