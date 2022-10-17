from sys import maxsize
from unittest.util import _MAX_LENGTH
from django.db import models
import time
from django.contrib.auth.models import User



class Merch(models.Model):

    name = models.CharField(max_length=300)
    img = models.CharField(max_length=450)
    bio = models.TextField(max_length=800)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class Review(models.Model):

    content = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    merch = models.ForeignKey(Merch, on_delete=models.CASCADE, related_name="reviews")


    def __str__(self):
        return self.content



class Wishlist(models.Model):

    title = models.CharField(max_length = 150, default = "Wishlist")
    merchs = models.ManyToManyField(Merch)

    def __str__(self):
        return self.title






