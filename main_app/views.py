from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Merch
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"



class MerchList(TemplateView):
    template_name = 'merch.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["merch"] = Merch.objects.filter(name__icontains=name)
            context["header"] = f"Results for '{name}'"
        else:
            context["merch"] = Merch.objects.all()
        return context


class ContactUs(TemplateView):
    template_name = "contact_us.html"



class MerchCreate(CreateView):
    model = Merch
    fields = ['name', 'img', 'bio']
    template_name = "merch_create.html"
    success_url = "/merch/"


class MerchDetail(DetailView):
    model = Merch
    template_name = "merch_detail.html"