from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('merch/', views.MerchList.as_view(), name = "merch"),
    path('contactus/', views.ContactUs.as_view(), name = 'contact_us'),
    path('merch/new/', views.MerchCreate.as_view(), name = "merch_create"),
    path('merch/<int:pk>/', views.MerchDetail.as_view(), name = "merch_detail"),
    path('merch/<int:pk>/update', views.MerchUpdate.as_view(), name = "merch_update"),
    path('merch/<int:pk>/delete', views.MerchDelete.as_view(), name = "merch_delete"),
    path('merch/<int:pk>/reviews/new/', views.ReviewCreate.as_view(), name = "review_create"),
    path('wishlists/<int:pk>/merchs/<int:merch_pk>/', views.WishlistMerchAssoc.as_view(), name= "wishlist_merch_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name = "signup")
]
