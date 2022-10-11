from django.db import models

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