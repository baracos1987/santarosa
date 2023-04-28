from django.contrib import admin
from.models import tarifas_motos, tarifas_carro, requisitos_tramites, inicial_carro_particular
from.models import traspaso_carro_particular, rematricula_carro_particular, remate_carro_particular, traspaso_indeter_carro_particular, cancelacion_licencia_carro_particular
from.models import cancela_licen_deterio_carro_particular, Dupli_Licencia_carro_parti, Inscrip_levanta_prenda_carro_parti,cambio_color_carro_parti, cambio_servicio_parti_publico
from.models import duplicado_placas_carro_parti, cambio_motor_regra_carro_parti,cambio_motor_carro_particular, cambio_carroce_otro_carro_particular, cambio_carroce_carro_particular
from.models import repotenciacion_carro_particular, radicado_carro_particular,transformacion_carro_particular



class TarifasAdmin(admin.ModelAdmin):
    list_display = ["descripcion_tarifa", "valor_tarifa", "valor_tarifa_RUNT", "valor_total"]
    #list_editable = ["valor_tarifa"] # campo editable en la columna valor tarifa
    search_fields = ["descripcion_tarifa"] # crear un input de busqueda
    list_filter = ["descripcion_tarifa"] # realizar por filtro
    list_per_page = 20 # paginacion, maximo 10 po hoja
    ordering = ["descripcion_tarifa"] # ordenar ascendentemente


# Registramos las tablas para mostrar en el admin, tambien llamamos la clase TarifasAdmin
admin.site.register(tarifas_motos, TarifasAdmin, group='grupo1')
admin.site.register(tarifas_carro, TarifasAdmin, group='grupo1')
admin.site.register(requisitos_tramites)
admin.site.register(inicial_carro_particular)
admin.site.register(traspaso_carro_particular)
admin.site.register(rematricula_carro_particular)
admin.site.register(remate_carro_particular)
admin.site.register(traspaso_indeter_carro_particular)
admin.site.register(cancelacion_licencia_carro_particular)
admin.site.register(cancela_licen_deterio_carro_particular) 
admin.site.register(Dupli_Licencia_carro_parti) 
admin.site.register(Inscrip_levanta_prenda_carro_parti) 
admin.site.register(cambio_color_carro_parti) 
admin.site.register(cambio_servicio_parti_publico)
admin.site.register(duplicado_placas_carro_parti)  
admin.site.register(cambio_motor_regra_carro_parti) 
admin.site.register(cambio_motor_carro_particular) 
admin.site.register(cambio_carroce_otro_carro_particular) 
admin.site.register(cambio_carroce_carro_particular) 
admin.site.register(repotenciacion_carro_particular)
admin.site.register(radicado_carro_particular)
admin.site.register(transformacion_carro_particular)  








