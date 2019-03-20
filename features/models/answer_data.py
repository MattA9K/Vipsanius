from django.db import models
from django.conf import settings
from django.urls.base import reverse



class Answer(models.Model):
    answer = models.TextField()
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(to=Question,
                                 on_delete=models.CASCADE)
    accepted = models.BooleanField(default=True,
                                   help_text="Author of question marks this as answered.")

    class Meta:
        ordering = ('-created',)

