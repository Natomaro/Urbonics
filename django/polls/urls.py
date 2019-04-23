from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^submit', views.submit),
    path('', views.index, name='index'),

]

