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
    return render(request, "leaflet/html/overview.html", {})

class ResourcesView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "maps/resources.html", {})

class ResourcesV_View(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/resources.html", {})
  
# Start of country/MFI views
#class kenya_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
#  group_required = ["KE", "VFI", "AFR"]
#  raise_exception = True
#  def get(self, request, *args, **kwargs):
#    COUNTRY = 'kenya'
#    country_list = s3resource.country_filter(self, COUNTRY)
#    return render(request, "maps/kenya.html", {'country_list' : country_list})
  
class kenya_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["KE", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'kenya'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/kenya.html", {'country_list' : country_list})
  
class malawi_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["MW", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'malawi'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/malawi.html", {'country_list' : country_list})
  
class tanzania_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["TZ", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'tanzania'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/tanzania.html", {'country_list' : country_list})
  
class uganda_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["UG", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'uganda'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/uganda.html", {'country_list' : country_list})

class zambia_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["ZM", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'zambia'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/zambia.html", {'country_list' : country_list})
  
class cambodia_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["KH", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'cambodia'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/cambodia.html", {'country_list' : country_list})
  
class myanmar_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["MM", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'myanmar'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/myanmar.html", {'country_list' : country_list})
  
class philippines_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["PH", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'philippines'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/philippines.html", {'country_list' : country_list})
  
class srilanka_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["LK", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'srilanka'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/srilanka.html", {'country_list' : country_list})
  
class ecuador_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["EC", "VFI", "LAR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'ecuador'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/ecuador.html", {'country_list' : country_list})
  
class honduras_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["HN", "VFI", "LAR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    COUNTRY = 'srilanka'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/srilanka.html", {'country_list' : country_list})
  
# End of country/MFI specific views

# Start of country/MFI views for interactive viewer
class kenyaV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["KE", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/kenya.html", {})
  
class malawiV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["MW", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/malawi.html", {})
  
class tanzaniaV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["TZ", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/tanzania.html", {})
  
class ugandaV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["UG", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/uganda.html", {})

class zambiaV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["ZM", "VFI", "AFR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/zambia.html", {})
  
class cambodiaV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["KH", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/cambodia.html", {})
  
class myanmarV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["MM", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/myanmar.html", {})
  
class philippinesV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["PH", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/philippines.html", {})
  
class srilankaV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["LK", "VFI", "ASR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/srilanka.html", {})
  
class ecuadorV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["EC", "VFI", "LAR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/ecuador.html", {})
  
class hondurasV_view(LoginRequiredMixin, GroupRequiredMixin, s3resource, View):
  group_required = ["HN", "VFI", "LAR"]
  raise_exception = True
  def get(self, request, *args, **kwargs):
    return render(request, "leaflet/html/honduras.html", {})
  
# End of country/MFI specific views for interactive viewer


class test(LoginRequiredMixin, s3resource, View):
  def get(self, request, *args, **kwargs):
    COUNTRY = 'kenya'
    country_list = s3resource.country_filter(self, COUNTRY)
    return render(request, "maps/test.html", {'country_list' : country_list})

