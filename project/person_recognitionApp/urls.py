from django.urls import path, re_path
from . import views

app_name = 'person_recognitionApp'

urlpatterns = [
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^loginCheck/$', views.loginCheck, name='loginCheck'),
]