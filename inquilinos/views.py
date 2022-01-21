from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Inquilinos, Unidades


def index(request):

    inquilinos = Inquilinos.objects.all()
    unidades = Unidades.objects.all()

    dados = {
        'inquilinos': inquilinos,
        'unidades': unidades,
    }
    return render(request, 'index.html', dados)


def inquilino(request, inquilino_id):
    inquilino = get_object_or_404(Inquilinos, pk=inquilino_id)

    inquilino_a_exibir = {
        'inquilino': inquilino
    }
    return render(request, 'inquilino.html', inquilino_a_exibir)


def unidade(request, numero_unidade):
    unidade = get_object_or_404(Unidades, pk=numero_unidade)

    unidade_a_exibir = {
        'unidade': unidade
    }
    return render(request, 'unidade.html', unidade_a_exibir)
