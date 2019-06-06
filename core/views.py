from django.shortcuts import render, redirect
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo, 
    MovMensalista, 
    Mensalista
)

from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MovMensalistaForm,
    MensalistaForm
)


def home(request):
    return render(request, 'core/index.html', {})


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


def pessoas_update(request, id):
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data ={
        'pessoa': pessoa,
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html',data)

def pessoas_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'pessoa': pessoa})

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


def veiculos_update(request, id):
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data = {
        'veiculo': veiculo,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculos.html', data)


def veiculos_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})

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


def mov_rot_update(request, id):
    mov_rot = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov_rot)
    data = {
        'mov_rot': mov_rot,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_mov_rot.html', data)


def mov_rot_delete(request, id):
    mov_rot = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        mov_rot.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov_rot})
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


def mov_mensalista_update(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
    data = {
        'mov_mensalista': mov_mensalista,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/update_mov_mensalista.html', data)

    
def mov_mensalista_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov_mensalista.delete()
        return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/delete_confirm.html', 
        {'obj': mov_mensalista})
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


def mensalista_update(request, id):
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data = {
        'mensalista': mensalista,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)


def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalista})
#--------FIM------------Cadastro MENSALISTAS----------------
