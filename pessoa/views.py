from django.shortcuts import render
from .form import PessoaForm
from .models import Pessoa
from django.urls import reverse
from django.views.generic import CreateView, DetailView,ListView




""" 
def pessoa_create(request):
    form=PessoaForm(request.POST or None)
    template_name='pessoas_form.html'

    if request.method=='POST':
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.save()

    context={
        'form':form,
        'model_name_plural':'Pessoas',
        

    }        
    return render(request, template_name,context) """

 
def pessoa_add(request):
    template_name='pessoas_form.html'
    return render(request,template_name)


class PessoaCreate(CreateView):
    model = Pessoa
    template_name = "pessoas_form.html"
    form_class=PessoaForm 

    def form_invalid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

class PessoaDetail(DetailView):
    model = Pessoa
    template_name = "pessoa_detail.html"
    queryset=Pessoa.objects.all()
        
class PessoaList(ListView):
    model=Pessoa
    template_name="pessoa_list.html"
    object=Pessoa.objects.all()    
            