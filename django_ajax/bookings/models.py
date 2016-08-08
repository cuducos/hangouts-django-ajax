from django.conf import settings
from django.db import models
from django.utils import timezone


class Booking(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='usuário')
    event = models.CharField('evento', max_length=128)
    date = models.DateField('data')
    created_on = models.DateTimeField('solicitado em', default=timezone.now)
    authorized = models.BooleanField('autorizado', default=False)

    class Meta:
        verbose_name = 'reserva'
        verbose_name_plural = 'reservas'
        ordering = ('-date',)

    def __str__(self):
        return self.event