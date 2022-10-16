from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Merch, Review, Wishlist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["wishlists"] = Wishlist.objects.all()
        return context



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
    def get_success_url(self):
        return reverse('merch_detail', kwargs={'pk': self.object.pk})


class MerchDetail(DetailView):
    model = Merch
    template_name = "merch_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["wishlists"] = Wishlist.objects.all()
        return context


class MerchUpdate(UpdateView):
    model = Merch
    fields = ['name', 'img', 'bio']
    template_name = "merch_update.html"

    def get_success_url(self):
        return reverse('merch_detail', kwargs={'pk': self.object.pk})


class MerchDelete(DeleteView):
    model = Merch
    template_name = "merch_delete_confirm.html"
    success_url = "/merch/"



class ReviewCreate(View):

    def post(self, request, pk):
        content = request.POST.get("content")
        rating = request.POST.get("rating")
        created = request.POST.get("created")
        merch = Merch.objects.get(pk=pk)
        Review.objects.create(content=content, rating=rating, merch=merch, created=created)
        return redirect('merch_detail', pk=pk)




class WishlistMerchAssoc(View):

    def get(self, request, pk, merch_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the wishlist by the id and
            # remove from the join table the given merch_id
            Wishlist.objects.get(pk=pk).merchs.remove(merch_pk)
        if assoc == "add":
            # get the wishlist by the id and
            # add to the join table the given merch_id
            Wishlist.objects.get(pk=pk).merchs.add(merch_pk)
        return redirect('home')
