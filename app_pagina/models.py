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