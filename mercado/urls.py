from django.urls import path
from mercado.views import home, cadastro_produto, buscar_produto, excluir_produto


urlpatterns = [
    path('', home), # Home
    path('processa_formulario/',cadastro_produto, name="processa_formulario"),
    path('itens/',buscar_produto, name="itens"),
    path('itens_exluidos/<int:id>',excluir_produto, name="excluindo"),
   
] 