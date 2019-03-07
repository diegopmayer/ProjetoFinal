from django.conf.urls import url
from .views import home, lista_pessoas

urlpatterns = [
    url('^$', home, name='core_home'),
    url('pessoas/', lista_pessoas, name='core_lista_pessoas'),
]
