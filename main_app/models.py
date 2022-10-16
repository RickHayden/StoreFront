from sys import maxsize
from unittest.util import _MAX_LENGTH
from django.db import models
# from accounts.models import Account

# Create your models here.

class Merch(models.Model):

    name = models.CharField(max_length=300)
    img = models.CharField(max_length=450)
    bio = models.TextField(max_length=800)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class Review(models.Model):

    content = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)
    merch = models.ForeignKey(Merch, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.content



class Wishlist(models.Model):

    title = models.CharField(max_length = 150, default = "Wishlist")
    content = models.ManyToManyField(Merch)

    def __str__(self):
        return self.title








# class ReviewRating(models.Model):
#     merch = models.ForeignKey(Merch, on_delete = models.CASCADE)
#     user = models.ForeignKey(Account, on_delete = models.CASCADE)
#     subject = models.CharField(max_length = 200, blank = True)
#     review = models.TextField(max_length = 500, blank = True)
#     rating = models.FloatField()
#     ip = models.CharField(max_length = 20, blank = True)
#     status = models.BooleanField(default = True)
#     created_date = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

#     def __str__(self):
#         return self.subject