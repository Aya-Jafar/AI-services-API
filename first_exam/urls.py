from django.urls import path
from . import views


urlpatterns = [
    path('',  views.MyExamView, name='my-exam-view'),
    
]
