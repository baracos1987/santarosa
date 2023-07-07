from django.shortcuts import render
from django.shortcuts import redirect# panel administrador *4
from django.urls import reverse #panel adminsitrador *4
import pandas as pd 

from .forms import RequisitosForm, RequisitosFormMoto
#from .forms import OpcionForm #importamos formulario de forms.py llamamos OpcionForm *7

#estas librerias es que llamar los datos de la tabla tarifas motos *5 
from django.shortcuts import render
from app_pagina.models import (tarifas_motos, tarifas_carro, inicial_carro_particular, traspaso_carro_particular, rematricula_carro_particular,
remate_carro_particular, traspaso_indeter_carro_particular, cancelacion_licencia_carro_particular, cancela_licen_deterio_carro_particular,
Dupli_Licencia_carro_parti, Inscrip_levanta_prenda_carro_parti, cambio_color_carro_parti, cambio_servicio_parti_publico,
duplicado_placas_carro_parti, cambio_motor_regra_carro_parti,cambio_motor_carro_particular, cambio_carroce_otro_carro_particular,
cambio_carroce_carro_particular, repotenciacion_carro_particular, radicado_carro_particular, transformacion_carro_particular, inicial_prenda_carro,
traspaso_prenda_carro_parti, blindaje_carro_parti, modifi_alerta_propi_carro_parti, modifi_alerta_acreedor_carro_parti, traslado_cuenta_carro_parti,
polarizado_carro_parti, cambio_conjunto_carro_parti, historial, inscripcion_RUNT, actualizacion_RUNT, expedicion_Licencia_Conduccion, 
cambio_documento1, cambio_documento2, inicial_moto, inicial_moto_prenda,traspaso_moto, traspaso_moto_prenda,radicado_moto, traslado_moto,
cancelacion_licencia_moto,duplicado_licencia_moto, inscribe_lev_prenda_moto, cambio_color_moto,duplicado_placa_moto,cambio_motor_regraba_moto,
cambio_motor_moto,rematricula_moto,transformacion_moto,indeterminado_moto, modificar_alerta_prop_moto, modificar_alerta_acree_moto,
cancela_licencia_moto,historial_moto)


# definimos una funcion para llamar un archivo de csv con pandas
def dataframe(request):
    path ='media/morosos.csv'
    df = pd.read_csv(path)
    return render(request, 'html/datos.html', {'dataframe':df})

# Creamos la vista para la base html
def home(request):
    return render(request, 'html/index.html')

def dashboard(request):
    return render(request, 'html/dashboard.html')

def educacion(request):
    return render(request, 'html/educacion.html')

def patrulleritos(request):
    return render(request, 'html/patrulleritos.html')

def tramites(request):
    return render(request, 'html/tramites.html')

def ubicacion(request):
    return render(request, 'html/ubicacion.html')

#def requisitos(request):
#    return render(request, 'html/requisitos.html')

def requisitosIndex(request):
    return render(request, 'html/requisitosIndex.html')

#redirecciona al panel del admin *4
def admin(request):
    return redirect(reverse('admin:index'))


#Funcion para traer los datos de la tabla tarifas motos al template tarifas.html *5
#utilizamos order_by para organizarlos ascendentemente
def tarifas(request):
    datos_tarifas_moto = tarifas_motos.objects.all().order_by('descripcion_tarifa')
    datos_tarifas_carro = tarifas_carro.objects.all().order_by('descripcion_tarifa')
    return render(request, 'html/tarifas.html', {'datos_tarifas_moto':datos_tarifas_moto, 
                                                 'datos_tarifas_carro':datos_tarifas_carro})

#Funcion para traer los datos de la tabla inicial_carro_particular y levarlos al template requisitos
#esta funcion nos permite buscar una id de una fila de la tabla tarifas_carro, luego nos trae el dato del campo valor_total y lo renderizamos al template requisitos

"""
def requisitos(request):
    #seleccionamo la fila y luego el campo que queremos mostrar, en este caso es para inicial carro particular
    fila = tarifas_carro.objects.get(id=1)
    campo_total_MI_carro = fila.valor_total
    
    fila2 = tarifas_carro.objects.get(id=3)
    campo_total_tras_carro = fila2.valor_total

    fila3 = tarifas_carro.objects.get(id=2)
    campo_total_Remat_carro = fila3.valor_total

    fila4 = tarifas_carro.objects.get(id=4)
    campo_total_Indeter_carro = fila4.valor_total
"""

"""
    #traemos todos los objetos o datos de la tabla, creamos variable y llamamos la tabla
    requisitos_inicial_carro_particular = inicial_carro_particular.objects.all()
    requisitos_traspaso_carro_particular = traspaso_carro_particular.objects.all()
    requisitos_rematricula_carro_particular = rematricula_carro_particular.objects.all()
    requisitos_remate_carro_particular = remate_carro_particular.objects.all()
    requisitos_traspaso_indeter_carro_particular = traspaso_indeter_carro_particular.objects.all()
    requisitos_cancela_licencia_carro_particular = cancelacion_licencia_carro_particular.objects.all()
    requisitos_cancela_lic_Dete_carro_particular = cancela_licen_deterio_carro_particular.objects.all()
    requisitos_Dupli_lic_tran_carro_particular = Dupli_Licencia_carro_parti.objects.all()
    requisitos_Inscri_levanta_carro_particular = Inscrip_levanta_prenda_carro_parti.objects.all()
    requisitos_Cambio_Color_carro_particular = cambio_color_carro_parti.objects.all()
    requisitos_Cambio_serv_particular_publico = cambio_servicio_parti_publico.objects.all()

    requisitos_duplicado_placa_carro_particular = duplicado_placas_carro_parti.objects.all()
    requisitos_cambio_motor_regra_carro_particular = cambio_motor_regra_carro_parti.objects.all()
    requisitos_cambio_motor__carro_particular = cambio_motor_carro_particular.objects.all()
    requisitos_cambio_carro_otro_carro_particular = cambio_carroce_otro_carro_particular.objects.all()
    requisitos_cambio_carro_carro_particular = cambio_carroce_carro_particular.objects.all()

    requisitos_repotenciacion_carro_particular = repotenciacion_carro_particular.objects.all()
    requisitos_radicado_carro_particular = radicado_carro_particular.objects.all()
    requisitos_transformacion_carro_particular= transformacion_carro_particular.objects.all()

    
    #luego hacemos un retorno con renderizacion de las siguientes variables
    return render(request, 'html/requisitos.html',{'requisitos_inicial_carro_particular':requisitos_inicial_carro_particular,
                                                   'campo_total_MI_carro':campo_total_MI_carro,
                                                   'requisitos_traspaso_carro_particular':requisitos_traspaso_carro_particular,
                                                   'campo_total_tras_carro':campo_total_tras_carro,
                                                   'requisitos_rematricula_carro_particular':requisitos_rematricula_carro_particular,
                                                   'campo_total_Remat_carro':campo_total_Remat_carro,
                                                   'requisitos_remate_carro_particular':requisitos_remate_carro_particular,
                                                   'requisitos_traspaso_indeter_carro_particular':requisitos_traspaso_indeter_carro_particular,
                                                   'campo_total_Indeter_carro':campo_total_Indeter_carro,
                                                   'requisitos_cancela_licencia_carro_particular':requisitos_cancela_licencia_carro_particular,
                                                   'requisitos_cancela_lic_Dete_carro_particular':requisitos_cancela_lic_Dete_carro_particular,
                                                   'requisitos_Dupli_lic_tran_carro_particular':requisitos_Dupli_lic_tran_carro_particular,
                                                   'requisitos_Inscri_levanta_carro_particular':requisitos_Inscri_levanta_carro_particular,
                                                   'requisitos_Cambio_Color_carro_particular':requisitos_Cambio_Color_carro_particular,
                                                   'requisitos_Cambio_serv_particular_publico':requisitos_Cambio_serv_particular_publico,
                                                   'requisitos_duplicado_placa_carro_particular':requisitos_duplicado_placa_carro_particular,
                                                   'requisitos_cambio_motor_regra_carro_particular':requisitos_cambio_motor_regra_carro_particular,
                                                   'requisitos_cambio_motor__carro_particular':requisitos_cambio_motor__carro_particular,
                                                   'requisitos_cambio_carro_otro_carro_particular':requisitos_cambio_carro_otro_carro_particular,
                                                   'requisitos_cambio_carro_carro_particular':requisitos_cambio_carro_carro_particular,
                                                   'requisitos_repotenciacion_carro_particular':requisitos_repotenciacion_carro_particular,
                                                   'requisitos_radicado_carro_particular':requisitos_radicado_carro_particular,
                                                   'requisitos_transformacion_carro_particular':requisitos_transformacion_carro_particular})
"""
# creamos una funcion para llamar los requerimientos vehiculos*7
def requisitosVehiculo(request):
    form = RequisitosForm(request.POST or None)
    results = []
    if form.is_valid():
        opcion = form.cleaned_data['opcion']
        if opcion == 'opcion1':
            results = inicial_carro_particular.objects.all()
        elif opcion == 'opcion3':
            results = traspaso_carro_particular.objects.all()
        elif opcion == 'opcion18':
            results = rematricula_carro_particular.objects.all()
        elif opcion == 'opcion20':
            results = remate_carro_particular.objects.all()
        elif opcion == 'opcion21':
            results = traspaso_indeter_carro_particular.objects.all()
        elif opcion == 'opcion25':
            results = cancelacion_licencia_carro_particular.objects.all()
        elif opcion == 'opcion7':
            results = cancela_licen_deterio_carro_particular.objects.all()
        elif opcion == 'opcion8':
            results = Dupli_Licencia_carro_parti.objects.all()
        elif opcion == 'opcion9':
            results = Inscrip_levanta_prenda_carro_parti.objects.all()
        elif opcion == 'opcion10':
            results = cambio_color_carro_parti.objects.all()
        elif opcion == 'opcion11':
            results = cambio_servicio_parti_publico.objects.all() 
        elif opcion == 'opcion12':
            results = duplicado_placas_carro_parti.objects.all()
        elif opcion == 'opcion13':
            results = cambio_motor_regra_carro_parti.objects.all()
        elif opcion == 'opcion14':
            results = cambio_motor_carro_particular.objects.all()
        elif opcion == 'opcion15':
            results = cambio_carroce_otro_carro_particular.objects.all()
        elif opcion == 'opcion16':
            results = cambio_carroce_carro_particular.objects.all()    
        elif opcion == 'opcion17':
            results = repotenciacion_carro_particular.objects.all()
        elif opcion == 'opcion5':
            results = radicado_carro_particular.objects.all()
        elif opcion == 'opcion19':
            results = transformacion_carro_particular.objects.all()
        elif opcion == 'opcion2':
            results = inicial_prenda_carro.objects.all()
        elif opcion == 'opcion4':
            results = traspaso_prenda_carro_parti.objects.all()
        elif opcion == 'opcion22':
            results = blindaje_carro_parti.objects.all()
        elif opcion == 'opcion23':
            results = modifi_alerta_propi_carro_parti.objects.all()
        elif opcion == 'opcion24':
            results = modifi_alerta_acreedor_carro_parti.objects.all()
        elif opcion == 'opcion6':
            results = traslado_cuenta_carro_parti.objects.all()
        elif opcion == 'opcion26':
            results = polarizado_carro_parti.objects.all()
        elif opcion == 'opcion27':
            results = cambio_conjunto_carro_parti.objects.all()
        elif opcion == 'opcion28':
            results = historial.objects.all()
        elif opcion == 'opcion29':
            results = inscripcion_RUNT.objects.all()
        elif opcion == 'opcion30':
            results = actualizacion_RUNT.objects.all()
        elif opcion == 'opcion31':
            results = expedicion_Licencia_Conduccion.objects.all()
        elif opcion == 'opcion32':
            results = cambio_documento1.objects.all()
        elif opcion == 'opcion33':
            results = cambio_documento2.objects.all()
       
    return render(request, 'html/requisitosVehiculo.html', {'form': form, 'results': results})


# creamos una funcion para llamar los requerimientos motos
def requisitosMoto(request):
    form = RequisitosFormMoto(request.POST or None)
    results = []
    if form.is_valid():
        opcion = form.cleaned_data['opcion']
        if opcion == 'opcion1':
            results = inicial_moto.objects.all()
        if opcion == 'opcion2':
            results = inicial_moto_prenda.objects.all()
        if opcion == 'opcion3':
            results = traspaso_moto.objects.all()
        if opcion == 'opcion4':
            results = traspaso_moto_prenda.objects.all()
        if opcion == 'opcion5':
            results = radicado_moto.objects.all()
        if opcion == 'opcion6':
            results = traslado_moto.objects.all()
        if opcion == 'opcion7':
            results = cancelacion_licencia_moto.objects.all()
        if opcion == 'opcion8':
            results = duplicado_licencia_moto.objects.all()  
        if opcion == 'opcion9':
            results = inscribe_lev_prenda_moto.objects.all()
        if opcion == 'opcion10':
            results = cambio_color_moto.objects.all()
        if opcion == 'opcion11':
            results = duplicado_placa_moto.objects.all()
        if opcion == 'opcion12':
            results = cambio_motor_regraba_moto.objects.all()
        if opcion == 'opcion13':
            results = cambio_motor_moto.objects.all()
        if opcion == 'opcion14':
            results = rematricula_moto.objects.all()
        if opcion == 'opcion15':
            results = transformacion_moto.objects.all()
        if opcion == 'opcion16':
            results = indeterminado_moto.objects.all()
        if opcion == 'opcion17':
            results = modificar_alerta_prop_moto.objects.all()
        if opcion == 'opcion18':
            results = modificar_alerta_acree_moto.objects.all()
        if opcion == 'opcion19':
            results = cancela_licencia_moto.objects.all()
        if opcion == 'opcion20':
            results = historial_moto.objects.all()
       
    return render(request, 'html/requisitosMoto.html', {'form': form, 'results': results})





    