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


