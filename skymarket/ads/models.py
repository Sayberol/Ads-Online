import datetime

from django.conf import settings
from django.db import models
from django.forms import DateTimeInput

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=20, default="test")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=3)
    description = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='ads/', null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=1000, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

