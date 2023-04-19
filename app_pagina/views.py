from django.shortcuts import render
from django.shortcuts import redirect# panel administrador *4
from django.urls import reverse #panel adminsitrador *4

#estas librerias es que llamar los datos de la tabla tarifas motos *5 
from django.shortcuts import render
from app_pagina.models import tarifas_motos, tarifas_carro 


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

#redirecciona al panel del admin *4
def admin(request):
    return redirect(reverse('admin:index'))

""" para eliminar
#Mostramos la tabla tarifas *5
def tarifas(request):
    return render(request, 'html/tarifas.html')
"""

#Funcion para pasar los datos de la tabla tarifas motos al template tarifas.html *5
def tarifas(request):
    datos_tarifas_moto = tarifas_motos.objects.all()
    datos_tarifas_carro = tarifas_carro.objects.all()
    return render(request, 'html/tarifas.html', {'datos_tarifas_moto':datos_tarifas_moto, 'datos_tarifas_carro':datos_tarifas_carro})








    