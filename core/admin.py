from django.contrib import admin
from .models import Pessoa, Marca, Veiculo, Parametros, MovRotativo


admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(MovRotativo)
