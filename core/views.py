from django.shortcuts import render, redirect
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo, 
    MovMensalista, 
    Mensalista)
from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MovMensalistaForm,
    MensalistaForm)


def home(request):
    context = {
        'mensagem': 'Hello World'
    }
    return render(request, 'core/index.html', context)


#--------INÍCIO------------Cadastro de Pessoas----------------
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    return render(request, 'core/lista_pessoas.html', 
        {'pessoas': pessoas, 'form': form})


def pessoas_add(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = PessoaForm()
    return redirect('core_lista_pessoas')
#--------FIM------------Cadastro de Pessoas----------------


#--------INÍCIO------------Cadastro de VEÍCULOS----------------
def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', 
        {'veiculos': veiculos, 'form': form})


def veiculos_add(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = VeiculoForm()
    return redirect('core_lista_veiculos')
#--------FIM------------Cadastro de VEÍCULOS----------------


#--------INÍCIO------------Cadastro de MOVIMENTAÇÕES ROTATIVOS----------------
def lista_movrotativos(request):
    form = MovRotativoForm()
    mov_rot = MovRotativo.objects.all()
    return render(request, 'core/lista_movrotativos.html', 
        {'mov_rot': mov_rot, 'form': form})


def mov_rot_add(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = MovRotativoForm()
    return redirect('core_lista_movrotativos')
#--------FIM------------Cadastro de MOVIMENTAÇÕES ROTATIVOS----------------


#--------INÍCIO------------Cadastro de MOVIMENTAÇÕES MENSALISTAS----------------
def lista_movmensalista(request):
    form = MovMensalistaForm()
    mov_mens = MovMensalista.objects.all()
    return render(request, 'core/lista_movmensalistas.html', 
        {'mov_mens': mov_mens, 'form': form})


def mov_mensalista_add(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = MovMensalistaForm()
    return redirect('core_lista_movmensalista')
#--------FIM------------Cadastro de MOVIMENTAÇÕES MENSALISTAS----------------


#--------INÍCIO------------Cadastro MENSALISTAS----------------
def lista_mensalista(request):
    form = MensalistaForm()
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', 
        {'mensalistas': mensalistas, 'form': form})


def mensalista_add(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = MensalistaForm()
    return redirect('core_lista_mensalista')
#--------FIM------------Cadastro MENSALISTAS----------------
