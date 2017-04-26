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


from maps.views import HomeView, AboutView, ContactView, DownloadView, ViewerView, kenya_view, malawi_view, tanzania_view, uganda_view, zambia_view, cambodia_view, myanmar_view, philippines_view, srilanka_view, ecuador_view, honduras_view, test

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^about/', AboutView.as_view()),
    url(r'^contact/', ContactView.as_view()),
    url(r'^download/overview/', DownloadView.as_view()),
    url(r'^download/test/', test.as_view()),
  #start of MFI urls
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
  #end of MFI urls
    url(r'^viewer/', ViewerView.as_view()),
    url(r'^accounts/', include('allauth.urls')),
]


  
