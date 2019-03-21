# Author - Matt Andrzejczuk

from django.views.generic import DayArchiveView

from features.models import Question

class DailyQuestionList(DayArchiveView):
    queryset = Question.objects.all()
    date_field = 'created'
    month_format = '%m'
    allow_empty = True
