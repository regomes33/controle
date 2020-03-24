from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome=models.CharField('nome',max_length=50)
    sobrenome=models.CharField('sobrenome',max_length=100)
    graduacao=models.CharField('graduacao',max_length=50)
    rg_funcional=models.CharField(blank=False, unique=True, max_length=7)
    cpf=models.CharField(blank=False,max_length=13, unique=True)

    class Meta:
        ordering=('nome',)
        verbose_name='nome'
        verbose_name_plural='nomes'

    def __str__(self):
        return ' '.join(filter(None,[self.graduacao,self.nome]))
