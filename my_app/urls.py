from django.urls import path
from . import views


urlpatterns = [
    path('',  views.MyView, name='my-view'),
    
]
