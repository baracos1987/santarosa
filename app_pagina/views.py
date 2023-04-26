from django.shortcuts import render
from django.shortcuts import redirect# panel administrador *4
from django.urls import reverse #panel adminsitrador *4


#estas librerias es que llamar los datos de la tabla tarifas motos *5 
from django.shortcuts import render
from app_pagina.models import tarifas_motos, tarifas_carro, inicial_carro_particular, traspaso_carro_particular, rematricula_carro_particular
from app_pagina.models import remate_carro_particular, traspaso_indeter_carro_particular, cancelacion_licencia_carro_particular, cancela_licen_deterio_carro_particular
from app_pagina.models import Dupli_Licencia_carro_parti, Inscrip_levanta_prenda_carro_parti, cambio_color_carro_parti, cambio_servicio_parti_publico
from app_pagina.models import duplicado_placas_carro_parti, cambio_motor_regra_carro_parti,cambio_motor_carro_particular, cambio_carroce_otro_carro_particular
from app_pagina.models import cambio_carroce_carro_particular, repotenciacion_carro_particular, radicado_carro_particular, transformacion_carro_particular

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

def requisitos(request):
    return render(request, 'html/requisitos.html')

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

    #traemos todos los objetos o datos de la tabla, creamos variable y llamamos la tabla
    requisitos_inicial_carro_particular = inicial_carro_particular.objects.all()
    requisitos_traspaso_carro_particular = traspaso_carro_particular.objects.all()
    requisitos_rematricula_carro_particular = rematricula_carro_particular.objects.all()
    requisitos_remate_carro_particular = remate_carro_particular.objects.all()
    requisitos_traspaso_indeter_carro_particular = traspaso_indeter_carro_particular.objects.all()
    requisitos_cancela_licencia_carro_particular = cancelacion_licencia_carro_particular.objects()
    requisitos_cancela_lic_Dete_carro_particular = cancela_licen_deterio_carro_particular.objects()
    requisitos_Dupli_lic_tran_carro_particular = Dupli_Licencia_carro_parti.objects()
    requisitos_Inscri_levanta_carro_particular = Inscrip_levanta_prenda_carro_parti.objects()
    requisitos_Cambio_Color_carro_particular = cambio_color_carro_parti.objects()
    requisitos_Cambio_serv_particular_publico = cambio_servicio_parti_publico.objects()
    requisitos_duplicado_placa_carro_particular = duplicado_placas_carro_parti.objects()
    requisitos_cambio_motor_regra_carro_particular = cambio_motor_regra_carro_parti.objects()
    requisitos_cambio_motor__carro_particular = cambio_motor_carro_particular.objects()
    requisitos_cambio_carro_otro_carro_particular = cambio_carroce_otro_carro_particular.objects()
    requisitos_cambio_carro_carro_particular = cambio_carroce_carro_particular.objects()
    requisitos_repotenciacion_carro_particular = repotenciacion_carro_particular.objects()
    requisitos_radicado_carro_particular = radicado_carro_particular.objects()
    requisitos_transformacion_carro_particular= transformacion_carro_particular.objects()

    
    

    
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






    