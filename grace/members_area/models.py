from django.db import models


class Registration(models.Model):
    username = models.CharField(max_length=51)
    password = models.CharField(max_length=36)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
