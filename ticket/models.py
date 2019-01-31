from django.db import models
from django.conf import settings
from django_fsm import FSMField


STATES = ('Новый', 'Назначен', 'Обрабатывается', 'Выполнен', 'Закрыт',
          'Отменен', 'Переоткрыт')
STATES = list(zip(STATES, STATES))


class Ticket(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    state = FSMField(default=STATES[0], choices=STATES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='author')
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name='responsible')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
