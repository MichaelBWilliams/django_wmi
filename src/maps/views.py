from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView
from braces.views import GroupRequiredMixin
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
  
# Start of country/MFI views
class kenya_view(LoginRequiredMixin, GroupRequiredMixin, View):

  group_required = "KE"
  raise_exception = True
  
  def get(self, request, *args, **kwargs):
    return render(request, "maps/kenya.html", {})
  
class malawi_view(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/malawi.html", {})
  
class tanzania_view(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/tanzania.html", {})
  
class uganda_view(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/uganda.html", {})
  
class zambia_view(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/zambia.html", {})
  
class cambodia_view(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/cambodia.html", {})
  
class myanmar_view(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/myanmar.html", {})
  
class philippines_view(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/philippines.html", {})
  
class srilanka_view(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/srilanka.html", {})
  
class ecuador_view(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/ecuador.html", {})
  
class honduras_view(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/honduras.html", {})
# End of country/MFI specific views

  

