from django.db import models

from eventex.subscriptions.validators import validate_cpf


class Subscription(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=15 , validators=[validate_cpf])
    email = models.EmailField('E-mail', blank=True)
    phone = models.CharField('Telefone',max_length=20, blank=True)
    paid = models.BooleanField('Pago', default=False)
    create_at = models.DateTimeField('Inscrito em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-create_at',)

    def __str__(self):
        return self.name