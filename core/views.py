from django.shortcuts import render
from .models import Pessoa

def home(request):
    context = {
        'mensagem': 'Hello World'
    }
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})
