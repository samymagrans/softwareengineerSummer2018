"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from carts.views import *

from .views import home_page, about_page, contact_page, login_page, register_page

# urlpatterns = [
#     url(r'^$', home_page),
#     url(r'^about/$', about_page),
#     url(r'^contact/$', contact_page),
#     url(r'^login/$', login_page),
#     url(r'admin/', admin.site.urls),
# ]
urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', login_page, name = 'login'),
    url(r'^cart/', include(("carts.urls",'carts'), namespace='cart')),
    url(r'^register/$', register_page, name='register'),
    url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^products/', include("products.urls", namespace=None)),
    url(r'^search/', include(('search.urls', 'search'), namespace='search')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

