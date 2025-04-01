from django.db import models

class Subscription(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=15)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefone',max_length=20)
    create_at = models.DateTimeField('Inscrito em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-create_at',)

    def __str__(self):
        return self.name