from django.conf.urls import url
from django.urls import path
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
    mensalista_add,
    pessoas_update,
    veiculos_update,
    mov_rot_update,
    mov_mensalista_update,
    mensalista_update,
    pessoas_delete,
    )

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^pessoas-add/$', pessoas_add, name='core_pessoas_add'),
    path('pessoas-update/<int:id>/', pessoas_update, name='core_pessoas_update'),
    path('pessoas-delete/<int:id>/', pessoas_delete, name='core_pessoas_delete'),

    url(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^veiculos-add/$', veiculos_add, name='core_veiculos_add'),
    path('veiculos-update/<int:id>/', veiculos_update, name='core_veiculos_update'),

    url(r'^mov-rot-list/$', lista_movrotativos, name='core_lista_movrotativos'),
    url(r'^mov-rot-add/$', mov_rot_add, name='core_mov_rot_add'),
    path('mov-rot-update/<int:id>/', mov_rot_update, name='core_mov_rot_update'),

    url(r'^mov-mensalistas/$', lista_movmensalista, 
        name='core_lista_movmensalista'),
    url(r'^mov-mensalistas-add/$', mov_mensalista_add, 
        name='core_mov_mensalista_add'),
    path('mov-mensalista-update/<int:id>/', mov_mensalista_update, name='core_mov_mensalista_update'),

    url(r'^mensalistas/$', lista_mensalista, name='core_lista_mensalista'),
    url(r'^mensalistas-add/$', mensalista_add, name='core_mensalista_add'),
    path('mensalista-update/<int:id>/', mensalista_update, name='core_mensalista_update'),
]
