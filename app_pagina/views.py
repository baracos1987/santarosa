from django.shortcuts import render

# Creamos la vista para la base html
def home(request):
    return render(request, 'html/base.html')
  