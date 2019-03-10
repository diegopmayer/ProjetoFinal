from django.conf.urls import url
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movrotativos, 
    lista_movmensalista, 
    lista_mensalista,
    pessoas_add,
    veiculos_add,
    mov_rot_add,
    mov_mensalista_add,
    mensalista_add)

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^pessoas-add/$', pessoas_add, name='core_pessoas_add'),
    url(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^veiculos-add/$', veiculos_add, name='core_veiculos_add'),
    url(r'^mov-rot-list/$', lista_movrotativos, name='core_lista_movrotativos'),
    url(r'^mov-rot-add/$', mov_rot_add, name='core_mov_rot_add'),
    url(r'^mov-mensalistas/$', lista_movmensalista, 
        name='core_lista_movmensalista'),
    url(r'^mov-mensalistas-add/$', mov_mensalista_add, 
        name='core_mov_mensalista_add'),
    url(r'^mensalistas/$', lista_mensalista, name='core_lista_mensalista'),
    url(r'^mensalistas-add/$', mensalista_add, name='core_mensalista_add'),
]
