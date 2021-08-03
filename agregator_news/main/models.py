from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='активация пройдена')

    send_message = models.BooleanField(default=True, verbose_name='Слать оповещение')


    class Meta(AbstractUser.Meta):
        pass


class Posts(models.Model):
    title = models.CharField(max_length=100, blank=True, default=str)
    link = models.CharField(max_length=150, blank=True, default=1)
    date = models.TextField(blank=True, default=str)
    text = models.TextField(blank=True, default=str)

    def __str__(self):
        return self.title

