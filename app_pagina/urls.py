from django.urls import path, include
from .views import home, dashboard, educacion, patrulleritos, tramites, tarifas, requisitos, requisitosIndex, requisitos2
from .import views # views para panel admin *4

#creamos la URL para llamar funcion home en la vista views
urlpatterns = [
    path('', home, name="home"),
    path('dashboard',dashboard, name="dashboard"),
    path('educacion',educacion,name="educacion" ),
    path('patrulleritos',patrulleritos,name='patrulleritos'),
    path('tramites', tramites,name='tramites'),
    path('admin/', views.admin, name='admin'), #ruta abrir panel admin *4
    path('tarifas', tarifas, name='tarifas'), 
    path('requisitos2', requisitos2, name='requisitos2'),
    path('requisitos', requisitos, name='requisitos'),
    path('requisitosIndex', requisitosIndex, name='requisitosIndex'),
   
    
    
    
]