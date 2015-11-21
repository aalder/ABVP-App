from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^volunteer/(?P<vol_id>[0-9]+)/$', views.volunteer, name='volunteer'),
    url(r'^volunteer/update/(?P<vol_id>[0-9]+)/$', views.update_profile_picture, name='volunteer-update'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^checkin/$', views.checkin, name='checkin'),
    url(r'^checkedout/$', views.open_logs, name='checkedout'),
    url(r'^available/$', views.available_vols, name='available'),
    url(r'^availabletasks/$', views.available_tasks, name='availabletasks'),
]