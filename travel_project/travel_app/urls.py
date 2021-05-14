
from django.urls import path

from . import views

urlpatterns = [

    path('', views.scr_print, name="scr_print"),

]