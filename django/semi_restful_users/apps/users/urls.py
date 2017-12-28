from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^new$', views.new),
	url(r'^(?P<user_id>\d+)/edit$', views.edit),
	url(r'^(?P<user_id>\d+)/show$', views.show),
	url(r'^create$', views.index),
	url(r'^(?P<user_id>\d+)/destroy$', views.destroy),
	url(r'^(?P<user_id>\d+)/update$', views.update),
]