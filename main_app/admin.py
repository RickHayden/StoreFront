from django.contrib import admin
from .models import Merch, Review, Wishlist

# Register your models here.
admin.site.register(Merch)
admin.site.register(Review)
admin.site.register(Wishlist)