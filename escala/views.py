from django.shortcuts import render
from .form import EscalaForm,ViaturaForm,EscalaIndividualForm
from .models import Escala
from django.urls import reverse
from django.views.generic import CreateView, DetailView,ListView

# Create your views here.

def escala_add(request):
    template_name='escala_form.html'
    return render(request,template_name)


class EscalaCreate(CreateView):
    model = Escala
    template_name = "escala_form.html"
    form_class=EscalaForm 

    def form_invalid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

""" class EscalaIndividualCreate(CreateView):
    model = Escala
    template_name = "escalaindividual_form.html"
    form_class=EscalaIndividualForm 

    def form_invalid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form) """

class ViaturaCreate(CreateView):
    model = Escala
    template_name = "viatura_form.html"
    form_class=ViaturaForm 

    def form_invalid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

class EscalaDetail(DetailView):
    model = Escala
    template_name = "escala_detail.html"
    queryset=Escala.objects.all()
        
class EscalaList(ListView):
    model=Escala
    template_name="escala_list.html"
    object=Escala.objects.all()    
            