from django.db import models
from django.db.models.signals import pre_save #para guarda en la base de datos *1
from django.dispatch import receiver # guarda en la base de datos *1





#-------------------------creamos la tabla tarifas motocicleta-----------------------------

class tarifas_motos(models.Model):
    descripcion_tarifa = models.CharField('Descripcion Tarifa',max_length=100, blank=False)
    valor_tarifa = models.IntegerField('Valor Tarifa TTO', blank=False)
    valor_tarifa_RUNT = models.IntegerField('Valor Tarifa RUNT', blank=False)
    valor_total = models.IntegerField('Valor Total', blank=True, default=0, editable=False)
    año = models.CharField('año tarifa', max_length=100, blank=True)          
        

    #colocamos un alias a la tabla tarifas_motos
    class Meta:
        verbose_name = 'tarifas_motos' #nombre de la tabla
        verbose_name_plural = 'Tarifas Motocicletas' #alias   

    #colocamos la descripcion_tarifa como campo principal
    def __str__(self):
        return self.descripcion_tarifa
    
    
#funcion para sumar dos campos y guardarlo en la base de datos *1
@receiver(pre_save, sender=tarifas_motos)
def calculate_sum(sender, instance, **kwargs):
    instance.valor_total = instance.valor_tarifa + instance.valor_tarifa_RUNT
    

 #-----------------------------creamos la tabla tarifas carro------------------------------

class tarifas_carro(models.Model):
    descripcion_tarifa = models.CharField('Descripcion Tarifa',max_length=100, blank=False)
    valor_tarifa = models.IntegerField('Valor Tarifa TTO', blank=False)
    valor_tarifa_RUNT = models.IntegerField('Valor Tarifa RUNT', blank=False)
    valor_total = models.IntegerField('Valor Total', blank=True, default=0, editable=False)
    año = models.CharField('año tarifa', max_length=100, blank=True)

    #colocamos un alias a la tabla tarifas_motos
    class Meta:
        verbose_name = 'tarifas_carro'
        verbose_name_plural ='Tarifas Carro'

    #colocamos la descripcion_tarifa como campo principal
    def __str__(self):
        return self.descripcion_tarifa 

#funcion para sumar dos campos y guardarlo en la base de datos *1
@receiver(pre_save, sender=tarifas_carro)
def calculate_sum(sender, instance, **kwargs):
    instance.valor_total = instance.valor_tarifa + instance.valor_tarifa_RUNT   

#-------------------------creamos la tabla requisitos-----------------------------
class requisitos_tramites(models.Model):
    descripcion = models.CharField('Descripcion', max_length=200, blank=False)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'requisitos_tramites'
        verbose_name_plural ='Requisitos Listado Tramites'

    #colocamos la descripcion como campo principal
    def __str__(self):
        return self.descripcion
#---------------creamos la tabla requisitos Inicial carro particular------------
class inicial_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'inicial_carro_particular'
        verbose_name_plural ='Requisitos Inicial Carro Particular'

    #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos traspaso carro particular------------
class traspaso_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'traspaso_carro_particular'
        verbose_name_plural ='Requisitos Traspaso Carro Particular'

    #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"


#---------------creamos la tabla requisitos Re matricula carro particular------------
class rematricula_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'rematricula_carro_particular'
        verbose_name_plural ='Requisitos ReMatricula Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos por remate carro particular------------
class remate_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'remate_carro_particular'
        verbose_name_plural ='Requisitos Remate Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos por traspaso indeterminado carro particular------------
class traspaso_indeter_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'indeterminado_carro_particular'
        verbose_name_plural ='Requisitos Traspaso Indeterminado Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos cancelacion licencia trnasito--------------------

class cancelacion_licencia_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'cancelacion_licencia_carro_particular'
        verbose_name_plural ='Requisitos Cancelacion licencia Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"
    
#---------------creamos la tabla requisitos cancelacion licencia trnasito--------------------

class cancela_licen_deterio_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'cancela_licen_deterio_carro_particular'
        verbose_name_plural ='Requisitos Cancelación licencia Deterioro Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos duplicado licencia de transito carro--------------------

class Dupli_Licencia_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'Dupli_Licencia_carro_parti'
        verbose_name_plural ='Requisitos Duplicado Licencia Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos Inscripcion o levantamiento prenda carro--------------------

class Inscrip_levanta_prenda_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'Inscrip_levanta_prenda_carro_parti'
        verbose_name_plural ='Requisitos Inscripcion o Levanta Prenda Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"
    
#---------------creamos la tabla requisitos cambio de color carro particular--------------------

class cambio_color_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'cambio_color_carro_parti'
        verbose_name_plural ='Requisitos Cambio Color Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"
    
#---------------creamos la tabla requisitos cambio servicio publico a particular--------------------

class cambio_servicio_parti_publico(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'cambio_servicio_parti_publico'
        verbose_name_plural ='Requisitos Cambio Publico a Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"


#---------------creamos la tabla requisitos duplicado placas carro particular----------------------

class duplicado_placas_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'duplicado_placas_carro_parti'
        verbose_name_plural ='Requisitos Duplicado Placa Carro particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos cambio motor regrabacion particular----------------------

class cambio_motor_regra_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'cambio_motor_regra_carro_parti'
        verbose_name_plural ='Requisitos Cambio Motor Regrabacion Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"
    
#---------------creamos la tabla requisitos cambio motor (vehiculo nuevo) carro particular--------------------

class cambio_motor_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'cambio_motor_carro_particular'
        verbose_name_plural ='Requisitos Cambio Motor Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---creamos la tabla requisitos cambio de carroceria (EN CASO DE SER DE OTRO VEHICULO) carro particular----

class cambio_carroce_otro_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'cambio_carroce_otro_carro_particular'
        verbose_name_plural ='Requisitos cambio Carroceria otro vehiculo carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"
    
#---------------creamos la tabla requisitos cambio de carroceria carro particular------------------

class cambio_carroce_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'cambio_carroce_carro_particular'
        verbose_name_plural ='Requisitos cambio Carroceria vehiculo carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos repotenciacion carro particular------------------

class repotenciacion_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'repotenciacion_carro_particular'
        verbose_name_plural ='Requisitos Repotenciacion Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos radicado de cuenta carro particular------------------

class radicado_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'radicado_carro_particular'
        verbose_name_plural ='Requisitos Radicado De CuentaCarro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos transformacion carro particular------------------

class transformacion_carro_particular(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'transformacion_carro_particular'
        verbose_name_plural ='Requisitos Transformacion Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#---------------creamos la tabla requisitos inicial y prenda carro particular------------------
class inicial_prenda_carro(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'inicial_prenda_carro'
        verbose_name_plural ='Requisitos Inicial Con Prenda Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-------------------creamos la tabla requisitos traspaso y prenda carro particular------------------
class traspaso_prenda_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'traspaso_prenda_carro_parti'
        verbose_name_plural ='Requisitos Traspaso y Prenda Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-----------------------creamos la tabla requisitos blindaje carro particular----------------------------
class blindaje_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'blindaje_carro_parti'
        verbose_name_plural ='Requisitos Blindaje Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-----------------------creamos la tabla requisitos MODIFICACION ALERTA PROPIETARIO.-----------------------
class modifi_alerta_propi_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'modifi_alerta_propi_carro_parti'
        verbose_name_plural ='Requisitos Modificacion Alerta Propietario Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-----------------------creamos la tabla requisitos MODIFICACION ALERTA ACREEDOR..-----------------------
class modifi_alerta_acreedor_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'modifi_alerta_acreedor_carro_parti'
        verbose_name_plural ='Requisitos Modificacion Alerta Acreedor Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-----------------------creamos la tabla requisitos Traslado de cuenta----------------------------
class traslado_cuenta_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'traslado_cuenta_carro_parti'
        verbose_name_plural ='Requisitos Traslado de cuenta Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-----------------------creamos la tabla requisitos polarizado----------------------------
class polarizado_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'polarizado_carro_parti'
        verbose_name_plural ='Requisitos Polarizado Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-----------------------creamos la tabla requisitos cambio conjunto----------------------------
class cambio_conjunto_carro_parti(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'cambio_conjunto_carro_parti'
        verbose_name_plural ='Requisitos Cambio Conjunto Carro Particular'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-----------------------creamos la tabla requisitos historial----------------------------
class historial(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'historial'
        verbose_name_plural ='Requisitos Historial'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-----------------------creamos la tabla requisitos Inscripcion RUNT----------------------------
class inscripcion_RUNT(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'Inscripcion_RUNT'
        verbose_name_plural ='Requisitos Inscripcion RUNT'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-----------------------creamos la tabla requisitos Actualizacion RUNT----------------------------
class actualizacion_RUNT(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'Actualizacion_RUNT'
        verbose_name_plural ='Requisitos Actualizacion RUNT'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#-----------------------creamos la tabla requisitos Exp licencia de conduccion----------------------------
class expedicion_Licencia_Conduccion(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'Expedicion_Licencia_Conduccion'
        verbose_name_plural ='Requisitos Expedicion Licencia Conduccion'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#----creamos la tabla requisitos ACTUALIZAR LICENCIA CONDUCCIÒN DE TARJETA DE IDENTIDAD A CEDULA ( DIFERENTE NUMERO) ---------
class cambio_documento1(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'Cambio_Documento1'
        verbose_name_plural ='Requisitos Cambio Documento Diferente Número'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"

#----creamos la tabla requisitos ACTUALIZAR LICENCIA CONDUCCIÒN DE TARJETA DE IDENTIDAD A CEDULA ( Mismo NUMERO) ---------
class cambio_documento2(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'Cambio_Documento2'
        verbose_name_plural ='Requisitos Cambio Documento Mismo Número'

        #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_carro.descripcion}"
    
#---------------   creamos la tabla requisitos Inicial moto  ---------------
class inicial_moto(models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'Inicial_Moto'
        verbose_name_plural ='Requisitos Inicial Motor'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos Inicial con prenda moto  ---------------
class inicial_moto_prenda (models.Model):
    requisitos_moto =models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'inicial_moto_prenda'
        verbose_name_plural ='Requisitos Inicial Motor Con Prenda'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos traspaso moto  ---------------
class traspaso_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'traspaso_moto'
        verbose_name_plural ='Requisitos Traspaso Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos traspaso moto prenda  ---------------
class traspaso_moto_prenda (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'traspaso_moto_prensa'
        verbose_name_plural ='Requisitos Traspaso Moto Con Prenda'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos radicado moto  ---------------
class radicado_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'radicado_moto'
        verbose_name_plural ='Requisitos Radicado Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos traslado moto  ---------------
class traslado_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'traslado_moto'
        verbose_name_plural ='Requisitos Traslado Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos cancelacion licencia moto  ---------------
class cancelacion_licencia_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'cancelacion_licencia_moto'
        verbose_name_plural ='Requisitos Cancelacion Licencia Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"
    
#---------------   creamos la tabla requisitos duplicado licencia moto  ---------------
class duplicado_licencia_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'duplicado_licencia_moto'
        verbose_name_plural ='Requisitos Duplicado Licencia Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos Inscribe levanta prenda moto  ---------------
class inscribe_lev_prenda_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'inscribe_lev_prenda_moto'
        verbose_name_plural ='Requisitos Inscribe Levanta Prenda Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos cambio de color moto  ---------------
class cambio_color_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'cambio_color_moto'
        verbose_name_plural ='Requisitos Cambio Color Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos cambio de color moto  ---------------
class duplicado_placa_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'duplicado_placa_moto'
        verbose_name_plural ='Requisitos Duplicado Placa Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos cambio de motor - regrabacion moto  ---------------
class cambio_motor_regraba_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'cambio_motor_regraba_moto'
        verbose_name_plural ='Requisitos Cambio Motor Regraba Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos cambio de motor - regrabacion moto  ---------------
class cambio_motor_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'cambio_motor_moto'
        verbose_name_plural ='Requisitos Cambio Motor Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos cambio de motor - regrabacion moto  ---------------
class rematricula_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'rematricula_moto'
        verbose_name_plural ='Requisitos Rematricula Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos transformacion moto  ---------------
class transformacion_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'transformacion_moto'
        verbose_name_plural ='Requisitos Transformacion Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos traspaso indeterminado moto ---------------
class indeterminado_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'indeterminado_moto'
        verbose_name_plural ='Requisitos Traspaso Indeterminado Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"



#---------------   creamos la tabla requisitos Modificación Alerta Propietario moto  ---------------
class modificar_alerta_prop_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'modificar_alerta_prop_moto'
        verbose_name_plural ='Requisitos Modificar Alerta Propietario Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos Modificación Alerta Acreedor moto  ---------------
class modificar_alerta_acree_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'modificar_alerta_acree_moto'
        verbose_name_plural ='Requisitos Modificar Alerta Acreedor Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos Cancelacion de Licencia moto  ---------------
class cancela_licencia_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'cancela_licencia_moto'
        verbose_name_plural ='Requisitos Cancelacion Licencia Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"

#---------------   creamos la tabla requisitos Historial Vehiculo Moto  ---------------
class historial_moto (models.Model):
    requisitos_moto = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla
    class Meta:
        verbose_name = 'historial_moto'
        verbose_name_plural ='Requisitos Historial Moto'
     #colocamos la descripcion como campo principal, este caso es cuando tenemos relación con otra tabla
    def __str__(self):
        return f"{self.requisitos_moto.descripcion}"