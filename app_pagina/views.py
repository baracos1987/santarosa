from django.shortcuts import render

# Creamos la vista para la base html
def home(request):
    return render(request, 'html/index.html')

def dashboard(request):
    return render(request, 'html/dashboard.html')

def educacion(request):
    return render(request, 'html/educacion.html')

def patrulleritos(request):
    return render(request, 'html/patrulleritos.html')
  