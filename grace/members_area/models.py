import uuid

from django.db import models


class Registration(models.Model):
    username = models.CharField('Usuário', max_length=51)
    password = models.CharField('Senha', max_length=36)
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    phone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail', max_length=75)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    hashId = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name = 'registro'
        verbose_name_plural = 'registros'
        ordering = ('-created_at', )

    def __str__(self):
        return self.name
