# Author - Matt Andrzejczuk

# from django.urls.conf import path
from django.urls import path

from features import views

app_name = "features"
urlpatterns = [
    path('q/<int:pk>/answer', views.CreateAnswerView.as_view(), name='answer_question'),
    path('a/<int:pk>/accept', views.UpdateAnswerAcceptance.as_view(), name='update_answer_acceptance'),
]

