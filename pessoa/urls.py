from django.urls import path
from pessoa import views as v
 

app_name='pessoa'

urlpatterns = [
    path('', v.PessoaList.as_view(),name='pessoa_list'), 
    path('add/', v.PessoaCreate.as_view(), name='pessoa_add'),
    path('<int:pk>',v.PessoaDetail.as_view(),name='pessoa_detail'),
    
 ]