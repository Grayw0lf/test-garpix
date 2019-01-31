# Generated by Django 2.1.5 on 2019-01-31 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('state', django_fsm.FSMField(choices=[('Новый', 'Новый'), ('Назначен', 'Назначен'), ('Обрабатывается', 'Обрабатывается'), ('Выполнен', 'Выполнен'), ('Закрыт', 'Закрыт'), ('Отменен', 'Отменен'), ('Переоткрыт', 'Переоткрыт')], default=('Новый', 'Новый'), max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('responsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsible', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
