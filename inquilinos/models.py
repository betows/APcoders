from django.db import models


class Unidades(models.Model):
    numero_unidade = models.IntegerField()
    proprietario_unidade = models.CharField(max_length=200)
    condominio_unidade = models.CharField(max_length=200)
    endereco_unidade = models.CharField(max_length=200)


class DespesaUnidades(models.Model):
    descricao_despesa_unidade = models.CharField(max_length=400)
    tipo_despesa_unidade = models.CharField(max_length=200)
    vencimento_fatura_unidade = models.CharField(max_length=100)
    status_pagamento_unidade = models.CharField(max_length=50)


class Inquilinos(models.Model):
    nome_inquilino = models.CharField(max_length=200)
    idade_inquilino = models.IntegerField()
    email_inquilino = models.EmailField()
    telefone_inquilino = models.IntegerField()
    sexo_inquilino = models.CharField(max_length=100)
