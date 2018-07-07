from django.conf.urls import url
#hello

from .views import SearchProductView


urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name='list'),
 ]

