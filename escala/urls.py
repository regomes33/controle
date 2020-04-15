from django.urls import path
from escala import views as v
 

app_name='escala'

urlpatterns = [
    path('', v.EscalaList.as_view(),name='escala_list'), 
    path('add/', v.EscalaCreate.as_view(), name='escala_add'),
    # path('add/', v.EscalaIndividualCreate.as_view(), name='escalaindividual_add'),
    path('add/',v.ViaturaCreate.as_view(),name='viatura_add'),
    path('<int:pk>',v.EscalaDetail.as_view(),name='escala_detail'),
   
    
 ]