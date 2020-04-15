from .models import Escala, Viatura
from django.forms import ModelForm


class EscalaForm(ModelForm):
   

    class Meta:
      

        model = Escala
        fields ='__all__'

class EscalaIndividualForm(ModelForm):
   

    class Meta:
      

        model = Escala
        fields =('rai','date','horas_trabalhada',)
class ViaturaForm(ModelForm):


    class Meta:
        model=Viatura
        fields='__all__'
