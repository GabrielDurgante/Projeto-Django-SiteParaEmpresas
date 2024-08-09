from django.shortcuts import render
from .models import Empresas

# Create your views here.
def cadastrar_empresa(request):
    if request.method == "GET":
        return render(request, 'cadastrar_empresa.html', {'tempo_existencia' : Empresas.tempo_existencia_choices,
                                                           'areas' : Empresas.area_choices, 
                                                           'publicos_alvos' : Empresas.publico_alvo_choices})