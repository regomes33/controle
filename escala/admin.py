from django.contrib import admin
from .models import Escala, Viatura

# Register your models here.
@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display=('__str__','rai')
    search_fields=('rai',)


@admin.register(Viatura)
class ViaturaAdmin(admin.ModelAdmin):
    list_display=('__str__',)
    search_fields=('viatura',)    


