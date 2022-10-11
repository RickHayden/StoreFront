from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('merch/', views.MerchList.as_view(), name = "merch"),
    path('contactus/', views.ContactUs.as_view(), name = 'contact_us')

]
