from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^volunteer/(?P<vol_id>[0-9]+)/$', views.volunteer, name='volunteer'),
    url(r'^checkout/$', views.checkout, name='checkout'),
]