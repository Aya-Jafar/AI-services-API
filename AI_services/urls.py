from django.urls import path
from .views import predict_next_word ,send_question ,summarize


urlpatterns = [
    path('next-word/',  predict_next_word),
    path("summarize/", summarize),
    path('QA/', send_question)
]
