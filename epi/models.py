from django.db import models

# Create your models here.

class EpiTipo(models.Model):
    descricao = models.CharField(max_length=50, unique=True, verbose_name='Descrição')
    
    class Meta:
        ordering = ['descricao']
        verbose_name = 'Tipo de EPI'
        verbose_name_plural = 'Tipos de EPI'

    def __str__(self):
        return self.descricao


class Epi(models.Model):
    especificacao = models.CharField(max_length=50, verbose_name='Especificação')
    tipo = models.ForeignKey(EpiTipo, on_delete=models.PROTECT, verbose_name='Tipo de EPI')

    class Meta:
        ordering = ['especificacao']
        verbose_name = 'EPI'
        verbose_name_plural = 'EPIs'

    def __str__(self):
        return f'{self.tipo.descricao} - {self.especificacao}'


class CA(models.Model):
    descricao = models.CharField(max_length=50, unique=True, verbose_name='Descrição')
    validade = models.DateField()
    tipos = models.ManyToManyField(EpiTipo)

    class Meta:
        ordering = ['descricao', 'validade']
        verbose_name = 'CA'
        verbose_name_plural = 'CAs'

    def __str__(self):
        return self.descricao
