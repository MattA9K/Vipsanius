# Author - Matt Andrzejczuk

# from django.urls.conf import path
from django.urls import path

from features import views

app_name = "features"
urlpatterns = [
    path('ask', views.AskQuestionView.as_view(), name='ask'),
    path('q/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail'),
]
