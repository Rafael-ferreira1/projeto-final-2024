from django.shortcuts import render
from .models import Supermercado
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request, 'mercado_template/pages/home.html', status=404)


def cadastro_produto(request):
    #salvando produto da tela no postegres
    novo_produto = Supermercado()
    novo_produto.produto = request.GET.get('produto')
    novo_produto.quantidade = request.GET.get('quantidade')
    novo_produto.categoria = request.GET.get('categoria')
    novo_produto.preço = request.GET.get('preco')
    novo_produto.save()
    #return HttpResponse('cadastrado realizado com sucesso')
    return render(request,'mercado_template/pages/home.html', status=404)

   

def buscar_produto(request):
    itens = {
        'itens': Supermercado.objects.all()
    }
    return render(request,'mercado_template/partials/itens.html',itens)


def excluir_produto(request, id):
    
    produto = Supermercado.objects.get(id=id)
    produto.delete()

    return redirect(buscar_produto)
   
     


def editar_produto(request):
    ...