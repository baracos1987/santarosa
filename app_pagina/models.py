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
    
#---------------creamos la tabla requisitos cambio servicio particular a publico--------------------

class cambio_servicio_parti_publico(models.Model):
    requisitos_carro = models.ForeignKey(requisitos_tramites, on_delete=models.CASCADE)

    #colocamos un alias a la tabla 
    class Meta:
        verbose_name = 'cambio_servicio_parti_publico'
        verbose_name_plural ='Requisitos Cambio Cambio Particular a Publico'

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