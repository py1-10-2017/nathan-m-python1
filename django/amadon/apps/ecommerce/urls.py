from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^amadon$', views.index),
	url(r'^total$', views.total),
	url(r'^checkout$', views.checkout),
	url(r'^clear$', views.clear_sessions)
]