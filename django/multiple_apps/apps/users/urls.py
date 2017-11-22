from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^register$', views.create),
	url(r'^login$', views.login),
	url(r'^users/new$', views.create),
	url(r'^users$', views.show),
]