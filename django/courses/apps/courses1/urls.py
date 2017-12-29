from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^(?P<course_id>\d+)/show$', views.show),
	url(r'^create$', views.index),
	url(r'^(?P<course_id>\d+)/destroy$', views.destroy),
]