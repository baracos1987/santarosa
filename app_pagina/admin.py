from django.contrib import admin
from.models import tarifas_motos

class TarifasAdmin(admin.ModelAdmin):
    list_display = ["descripcion_tarifa", "valor_tarifa"]
    list_editable = ["valor_tarifa"] # campo editable en la columna valor tarifa
    search_fields = ["descripcion_tarifa"] # crear un input de busqueda
    list_filter = ["descripcion_tarifa"] # realizar por filtro
    list_per_page = 15 # paginacion, maximo 10 po hoja



# Register your models here.
admin.site.register(tarifas_motos, TarifasAdmin)