from django.shortcuts import render
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo, 
    MovMensalista, 
    Mensalista
)
from .forms import PessoaForm

def home(request):
    context = {
        'mensagem': 'Hello World'
    }
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    return render(request, 'core/lista_pessoas.html', 
        {'pessoas': pessoas, 'form': form})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    return render(request, 'core/lista_movrotativos.html', {'mov_rot': mov_rot})


def lista_movmensalista(request):
    mov_mens = MovMensalista.objects.all()
    return render(request, 'core/lista_movmensalista.html', {'mov_mens': mov_mens})


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', 
        {'mensalistas': mensalistas})
