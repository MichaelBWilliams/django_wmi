from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Map

# Create your views here.

class HomeView(LoginRequiredMixin, View):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  def get(self, request, *args, **kwargs):
    return render(request, "maps/home.html", {})

  

