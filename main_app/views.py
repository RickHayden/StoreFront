from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"



class Merch(TemplateView):
    template_name = "merch.html"


class ContactUs(TemplateView):
    template_name = "contact_us.html"