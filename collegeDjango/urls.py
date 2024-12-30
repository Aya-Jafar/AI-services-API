
from django.urls import path , include 
from django.contrib import admin




urlpatterns = [
    path('admin/',admin.site.urls),

    # path('exam/', include('first_exam.urls')),
    path('generate/', include('AI_services.urls')),
]

