from django.db import models
from django.forms import CharField

# Create your models here.


class Supermercado(models.Model):
    id = models.AutoField(primary_key=True)
    produto = models.CharField(max_length=50, default=None)
    categoria = models.CharField(max_length=50, default=None)
    quantidade = models.IntegerField(null=True, default=None)
    #preço = models.IntegerField(null=True, default=None)
    preço = models.DecimalField(null=True, max_digits=5, decimal_places=2, default=None)

