from django.contrib.auth.decorators import login_required
from django.urls import include, path

from cadastros.views import CidadeList, CidadeDetail, CidadeDelete, CidadeCreate, CidadeUpdate, EstadoCreate, PaisCreate

urlpatterns = [
    path('', CidadeList.as_view(), name='cidades-list'),
    path('detail/<int:pk>/', CidadeDetail.as_view(), name='cidades-detalhe'),
    path('delete/<int:pk>/', login_required(CidadeDelete.as_view()), name='cidades-remove'),
    path('update/<int:pk>/', login_required(CidadeUpdate.as_view()), name='cidades-editar'),
    path('create/', login_required(CidadeCreate.as_view()), name='cidades-cadastro'),
    path('createestado/', login_required(EstadoCreate.as_view()), name='estados-cadastro'),
    path('createpais/', login_required(PaisCreate.as_view()), name='paises-cadastro')
]