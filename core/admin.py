from django.contrib import admin
from .models import Pessoa, Marca, Veiculo, Parametros, MovRotativo, Mensalista, MovMensalista

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin', 'checkout', 'valor_hora', 'pago', 'total', 'horas_total', 'veiculo')


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'mensalista', 'dt_pgto', 'total')


admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)