from django.db import models
from django.conf import settings
from django_fsm import FSMField, transition


class Ticket(models.Model):
    # ('Новый', 'Назначен', 'Обрабатывается', 'Выполнен', 'Закрыт',
    #         'Отменен', 'Переоткрыт')
    STATES = ('New', 'Assigned', 'In Progress', 'Fulfilled', 'Closed',
              'Chanceled', 'Re Opened')
    STATES = list(zip(STATES, STATES))

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
