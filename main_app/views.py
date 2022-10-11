from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Merch

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"



class MerchList(TemplateView):
    template_name = 'merch.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["merch"] = Merch.objects.all() # Here we are using the model to query the database for us.
        return context


class ContactUs(TemplateView):
    template_name = "contact_us.html"



    