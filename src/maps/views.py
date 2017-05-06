from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Map, s3resource

# Create your views here.
class TestView(View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/test.html", {})

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

class ResourcesView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/resources.html", {})
  
# Start of country/MFI views
class kenya_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["KE", "VFI", "AFR"]
  raise_exception = True
  #mapmatrix = "mapmatrixFAKE"
  def get(self, request, *args, **kwargs):
    COUNTRY = 'kenya'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/kenya.html", {'country_list' : country_list})
  
class malawi_view(LoginRequiredMixin, GroupRequiredMixin, View):
  group_required = ["MW", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "maps/malawi.html", {})
  
class tanzania_view(LoginRequiredMixin, GroupRequiredMixin, View):
  group_required = ["TZ", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "maps/tanzania.html", {})
  
class uganda_view(LoginRequiredMixin, GroupRequiredMixin, View):
  group_required = ["UG", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "maps/uganda.html", {})
  
class zambia_view(LoginRequiredMixin, GroupRequiredMixin, View):
  group_required = ["ZM", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "maps/zambia.html", {})
  
class cambodia_view(LoginRequiredMixin, GroupRequiredMixin, View):
  group_required = ["KH", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "maps/cambodia.html", {})
  
class myanmar_view(LoginRequiredMixin, GroupRequiredMixin, View):
  group_required = ["MM", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "maps/myanmar.html", {})
  
class philippines_view(LoginRequiredMixin, GroupRequiredMixin, View):
  group_required = ["PH", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "maps/philippines.html", {})
  
class srilanka_view(LoginRequiredMixin, GroupRequiredMixin, View):
  group_required = ["LK", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "maps/srilanka.html", {})
  
class ecuador_view(LoginRequiredMixin, GroupRequiredMixin, View):
  group_required = ["EC", "VFI", "LAR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "maps/ecuador.html", {})
  
class honduras_view(LoginRequiredMixin, GroupRequiredMixin, View):
  group_required = ["HN", "VFI", "LAR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "maps/honduras.html", {})
# End of country/MFI specific views

class test(LoginRequiredMixin, s3resource, View):
  def get(self, request, *args, **kwargs):
    COUNTRY = 'kenya'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/test.html", {'country_list' : country_list})

