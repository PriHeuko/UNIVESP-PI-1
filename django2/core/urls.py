from django.urls import path

from .views import index, contato, produto, listaProdutos



urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('listaProdutos/', listaProdutos, name='listaProdutos'),
]