from django.contrib import admin
from.models import tarifas_motos, tarifas_carro

class TarifasAdmin(admin.ModelAdmin):
    list_display = ["descripcion_tarifa", "valor_tarifa", "valor_tarifa_RUNT", "valor_total"]
    #list_editable = ["valor_tarifa"] # campo editable en la columna valor tarifa
    search_fields = ["descripcion_tarifa"] # crear un input de busqueda
    list_filter = ["descripcion_tarifa"] # realizar por filtro
    list_per_page = 20 # paginacion, maximo 10 po hoja
    ordering = ["descripcion_tarifa"] # ordenar ascendentemente



    
    

# Register your models here.
admin.site.register(tarifas_motos, TarifasAdmin)
admin.site.register(tarifas_carro, TarifasAdmin)