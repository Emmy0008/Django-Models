from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

class Post (models.Model):
    Title = models.CharField(max_length=23, default="")
    Text = models.CharField(max_length=23, default="")
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default='')
    Created_Date = models.DateTimeField()
    Published_Date = models.DateTimeField()
    # def __str__(self) -> str:
    #     return self.name