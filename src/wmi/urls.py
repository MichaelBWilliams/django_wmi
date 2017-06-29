"""wmi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


from maps.views import TestView, HomeView, AboutView, ContactView, DownloadView, ViewerView, kenya_view, malawi_view, tanzania_view, uganda_view, zambia_view, cambodia_view, myanmar_view, philippines_view, srilanka_view, ecuador_view, honduras_view, kenyaV_view, malawiV_view, tanzaniaV_view, ugandaV_view, zambiaV_view, cambodiaV_view, myanmarV_view, philippinesV_view, srilankaV_view, ecuadorV_view, hondurasV_view, test, ResourcesView, ResourcesV_View

urlpatterns = [
    url(r'^test/', TestView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^about/', AboutView.as_view()),
    url(r'^contact/', ContactView.as_view()),
    url(r'^resources/', ResourcesView.as_view()),
	  url(r'^viewer/resources/', ResourcesV_View.as_view()),
    url(r'^download/overview/', DownloadView.as_view()),
    url(r'^download/test/', test.as_view()),
    url(r'^viewer/overview/', ViewerView.as_view()),
  
  #start of MFI download urls
    url(r'^download/kenya/', kenya_view.as_view()),
    url(r'^download/malawi/', malawi_view.as_view()),
    url(r'^download/tanzania/', tanzania_view.as_view()),
    url(r'^download/uganda/', uganda_view.as_view()),
    url(r'^download/zambia/', zambia_view.as_view()),
    url(r'^download/cambodia/', cambodia_view.as_view()),
    url(r'^download/myanmar/', myanmar_view.as_view()),
    url(r'^download/philippines/', philippines_view.as_view()),
    url(r'^download/srilanka/', srilanka_view.as_view()),
    url(r'^download/ecuador/', ecuador_view.as_view()),
    url(r'^download/honduras/', honduras_view.as_view()),
  #end of MFI download urls
		url(r'^viewer/kenya/', kenyaV_view.as_view()),
    url(r'^viewer/malawi/', malawiV_view.as_view()),
    url(r'^viewer/tanzania/', tanzaniaV_view.as_view()),
    url(r'^viewer/uganda/', ugandaV_view.as_view()),
    url(r'^viewer/zambia/', zambiaV_view.as_view()),
    url(r'^viewer/cambodia/', cambodiaV_view.as_view()),
    url(r'^viewer/myanmar/', myanmarV_view.as_view()),
    url(r'^viewer/philippines/', philippinesV_view.as_view()),
    url(r'^viewer/srilanka/', srilankaV_view.as_view()),
    url(r'^viewer/ecuador/', ecuadorV_view.as_view()),
    url(r'^viewer/honduras/', hondurasV_view.as_view()),
	
	#Start of MFI interactive map viewer urls
	

    url(r'^accounts/', include('allauth.urls')),
]


  
