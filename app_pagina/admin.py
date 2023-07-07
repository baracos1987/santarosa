from django.contrib import admin
from.models import (tarifas_motos, tarifas_carro, requisitos_tramites, inicial_carro_particular,
 traspaso_carro_particular, rematricula_carro_particular, remate_carro_particular, traspaso_indeter_carro_particular, 
 cancelacion_licencia_carro_particular, cancela_licen_deterio_carro_particular, Dupli_Licencia_carro_parti, 
 Inscrip_levanta_prenda_carro_parti,cambio_color_carro_parti, cambio_servicio_parti_publico,duplicado_placas_carro_parti, 
 cambio_motor_regra_carro_parti,cambio_motor_carro_particular, cambio_carroce_otro_carro_particular, cambio_carroce_carro_particular,
 repotenciacion_carro_particular, radicado_carro_particular,transformacion_carro_particular, inicial_prenda_carro, 
 traspaso_prenda_carro_parti, blindaje_carro_parti, modifi_alerta_propi_carro_parti, modifi_alerta_acreedor_carro_parti,
 traslado_cuenta_carro_parti, polarizado_carro_parti, cambio_conjunto_carro_parti, historial, inscripcion_RUNT, actualizacion_RUNT,
 expedicion_Licencia_Conduccion, cambio_documento1, cambio_documento2, inicial_moto, inicial_moto_prenda, traspaso_moto,
 traspaso_moto_prenda, radicado_moto, traslado_moto, cancelacion_licencia_moto, duplicado_licencia_moto, inscribe_lev_prenda_moto, cambio_color_moto,
 duplicado_placa_moto,cambio_motor_regraba_moto,cambio_motor_moto,rematricula_moto,transformacion_moto,indeterminado_moto,
 modificar_alerta_prop_moto, modificar_alerta_acree_moto, cancela_licencia_moto,historial_moto) 



class TarifasAdmin(admin.ModelAdmin):
    list_display = ["descripcion_tarifa", "valor_tarifa", "valor_tarifa_RUNT", "valor_total"]
    #list_editable = ["valor_tarifa"] # campo editable en la columna valor tarifa
    search_fields = ["descripcion_tarifa"] # crear un input de busqueda
    list_filter = ["descripcion_tarifa"] # realizar por filtro
    list_per_page = 20 # paginacion, maximo 10 po hoja
    ordering = ["descripcion_tarifa"] # ordenar ascendentemente


# Registramos las tablas para mostrar en el admin, tambien llamamos la clase TarifasAdmin
admin.site.register(tarifas_motos, TarifasAdmin)
admin.site.register(tarifas_carro, TarifasAdmin)
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
admin.site.register(inicial_prenda_carro)
admin.site.register(traspaso_prenda_carro_parti)
admin.site.register(blindaje_carro_parti)
admin.site.register(modifi_alerta_propi_carro_parti)
admin.site.register(modifi_alerta_acreedor_carro_parti)
admin.site.register(traslado_cuenta_carro_parti)
admin.site.register(polarizado_carro_parti)
admin.site.register(cambio_conjunto_carro_parti)
admin.site.register(historial)
admin.site.register(inscripcion_RUNT)
admin.site.register(actualizacion_RUNT)
admin.site.register(expedicion_Licencia_Conduccion)
admin.site.register(cambio_documento1)
admin.site.register(cambio_documento2)
admin.site.register(inicial_moto)
admin.site.register(inicial_moto_prenda)
admin.site.register(traspaso_moto)
admin.site.register(traspaso_moto_prenda) 
admin.site.register(radicado_moto)
admin.site.register(traslado_moto) 
admin.site.register(cancelacion_licencia_moto) 
admin.site.register(duplicado_licencia_moto) 
admin.site.register(inscribe_lev_prenda_moto)
admin.site.register(cambio_color_moto)
admin.site.register(duplicado_placa_moto) 
admin.site.register(cambio_motor_regraba_moto) 
admin.site.register(cambio_motor_moto)
admin.site.register(rematricula_moto) 
admin.site.register(transformacion_moto) 
admin.site.register(indeterminado_moto)
admin.site.register(modificar_alerta_prop_moto) 
admin.site.register(modificar_alerta_acree_moto)
admin.site.register(cancela_licencia_moto)
admin.site.register(historial_moto)
















