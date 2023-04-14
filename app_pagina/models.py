from django.db import models

# Create your models here.

#creamos la tabla tarifas motocicleta
class tarifas_motos(models.Model):
    descripcion_tarifa = models.CharField('Descripcion Tarifa',max_length=100, blank=False)
    valor_tarifa = models.IntegerField('Valor Tarifa', blank=False)
    año = models.CharField('año tarifa', max_length=100, blank=True)


    #colocamos un alias a la tabla tarifas_motos
    class Meta:
        verbose_name = 'tarifas_motos' #nombre de la tabla
        verbose_name_plural = 'Tarifas Motocicletas' #alias
       


    #colocamos la descripcion_tarifa como campo principal
    def __str__(self):
        return self.descripcion_tarifa
    

   
    
    

   



