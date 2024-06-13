from django.shortcuts import render
from .models import Supermercado
from django.http import HttpResponse
from django.shortcuts import redirect
from decimal import Decimal
# Create your views here.

def home(request):
    return render(request, 'mercado_template/pages/home.html', status=404)


def cadastro_produto(request):
    #salvando produto da tela no postegres
    novo_produto = Supermercado()
    novo_produto.produto = request.GET.get('produto')
    novo_produto.quantidade = request.GET.get('quantidade')
    novo_produto.categoria = request.GET.get('categoria')
    novo_produto.preço =(request.GET.get('preco'))
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

def editar_produto(request, id):
    produto = Supermercado.objects.get(id=id)
        
    return render(request, "mercado_template/partials/update.html", {"produto": produto})
    

def editar_produto_dois(request, id):
    
    novo_produto1 = request.GET.get('produto')
    novo_produto2 = request.GET.get('quantidade')
    novo_produto3 = request.GET.get('categoria')
    novo_produto4 =(request.GET.get('preco')) #request.GET.get('preço') antes estava assim.
    produto = Supermercado.objects.get(id=id)
    
    produto.produto = novo_produto1
    produto.quantidade = novo_produto2
    produto.categoria = novo_produto3
    produto.preço = novo_produto4
    produto.save()
      
    return redirect(buscar_produto)



# função converter preços

def reverte(dado):
    rev = dado[3:8]  # print '19,90'  str
   # substituir o caracter ',' por '.'
pass

     


