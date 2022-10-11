from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('merch/', views.MerchList.as_view(), name = "merch"),
    path('contactus/', views.ContactUs.as_view(), name = 'contact_us'),
    path('merch/new/', views.MerchCreate.as_view(), name = "merch_create"),
    path('merch/<int:pk>/', views.MerchDetail.as_view(), name = "merch_detail")
]
