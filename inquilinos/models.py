from django.db import models


class inquilino(models.Model):
    nome_inquilino = models.CharField(max_length=200)
    idade_inquilino = models.IntegerField()
    email_inquilino = models.EmailField()
    telefone_inquilino = models.IntegerField()
    sexo_inquilino = models.CharField(max_length=100)
