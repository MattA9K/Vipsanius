# Author - Matt Andrzejczuk
from django.views.generic import DetailView

from features.posts import AnswerForm, AnswerAcceptanceForm
from features.models import Question


class QuestionDetailView(DetailView):
    model = Question

    ACCEPTANCE_FORM = AnswerAcceptanceForm(initial={'accepted': True})
    REJECT_FORM = AnswerAcceptanceForm(initial={'accepted': False})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'answer_form': AnswerForm(initial={
                'user': self.request.user.id,
                'question': self.object.id,
            })
        })
        if self.object.can_accept_answers(self.request.user):
            ctx.update({
                'accept_form': self.ACCEPTANCE_FORM,
                'reject_form': self.REJECT_FORM,
            })
        return ctx
