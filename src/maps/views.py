from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Map

# Create your views here.

class HomeView(LoginRequiredMixin, View):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  def get(self, request, *args, **kwargs):
    return render(request, "maps/home.html", {})
  
class AboutView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/about.html", {})
  
class ContactView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/contact.html", {})
  
class DownloadView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/download.html", {})
  
class ViewerView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/viewer.html", {})
  

  

