from django.db import models
from pessoa.models import Pessoa

# Create your models here.

TIPOVTR=(
    ('oficial','Oficial'),
    ('reserva','Reserva'),

)



class Viatura(models.Model):
    
    viatura=models.CharField('viatura',max_length=20)
    tipo=models.CharField('tipo',max_length=20,choices=TIPOVTR)




    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'viatura'
        verbose_name_plural = 'viatura'

    def __str__(self):
        return str(self.viatura)

SERVICOS=(
    ('extraordinario','Extraordinário'),
    ('odrinario','Ordinário'),
)

class Escala (models.Model):
    pessoa=models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    viatura=models.ForeignKey(Viatura,on_delete=models.PROTECT)
    rai=models.IntegerField('rai',)
    date=models.DateField('Data da Escala')
    horas_trabalhada=models.CharField('Horas', max_length=3)
    servico=models.CharField('Servico', max_length=20, choices=SERVICOS)
    quilometragem= models.IntegerField('KM',)




    

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'rai'
        verbose_name_plural = 'rais'

    def __str__(self):
        return str(self.rai)
