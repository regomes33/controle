from django.forms import ModelForm
   
from .models import Pessoa

class PessoaForm(ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Pessoa
        fields ='__all__'
