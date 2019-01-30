from django.db import models
from django.contrib.auth.models import User


class Sala(models.Model):
    nomeSala = models.CharField('Nome Sala', max_length=120, null=True, blank=True)
    hash = models.CharField('Sala ID', max_length=500, null=True, blank=True)
    userTx = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="userTX")
    userRx = models.ManyToManyField(User, null=True, blank=True)


    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now_add=True)