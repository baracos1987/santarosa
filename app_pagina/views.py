from django.shortcuts import render
from django.shortcuts import redirect# panel administrador *4
from django.urls import reverse #panel adminsitrador *4

#estas librerias es que llamar los datos de la tabla tarifas motos *5 
from django.shortcuts import render
from app_pagina.models import tarifas_motos, tarifas_carro, inicial_carro_particular, traspaso_carro_particular, rematricula_carro_particular


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

    #traemos todos los objetos o datos de la tabla 
    requisitos_inicial_carro_particular = inicial_carro_particular.objects.all()
    requisitos_traspaso_carro_particular = traspaso_carro_particular.objects.all()
    requisitos_rematricula_carro_particular = rematricula_carro_particular.objects.all()
    #luego hacemos un retorno con renderizacion de las siguientes variables
    return render(request, 'html/requisitos.html',{'requisitos_inicial_carro_particular':requisitos_inicial_carro_particular,
                                                   'campo_total_MI_carro':campo_total_MI_carro,
                                                   'requisitos_traspaso_carro_particular':requisitos_traspaso_carro_particular,
                                                   'campo_total_tras_carro':campo_total_tras_carro,
                                                   'requisitos_rematricula_carro_particular':requisitos_rematricula_carro_particular,
                                                   'campo_total_Remat_carro':campo_total_Remat_carro})






    