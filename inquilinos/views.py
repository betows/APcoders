from django.shortcuts import render


def index(request):

    inquilinos = {
        1: 'Roberto Amaral',
        2: 'Maria Venera',
        3: 'Isadora Spada'
    }

    dados = {
        'nome_inquilino': inquilinos
    }
    return render(request, 'index.html', dados)


def inquilino(request):
    return render(request, 'inquilino.html')


def unidade(request):
    return render(request, 'unidade.html')
