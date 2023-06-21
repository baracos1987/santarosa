from django.urls import path, include
from .views import home, dashboard, educacion, patrulleritos, tramites, tarifas, requisitosIndex, requisitosVehiculo, ubicacion, dataframe, requisitosMoto
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
    path('requisitosVehiculo', requisitosVehiculo, name='requisitosVehiculo'),
    # path('requisitos', requisitos, name='requisitos'), es para eliminar el codigo
    path('requisitosIndex', requisitosIndex, name='requisitosIndex'),
    path('ubicacion',ubicacion, name='ubicacion'),
    path('dataframe',dataframe,name='dataframe'),
    path('requisitosMoto', requisitosMoto, name='requisitosMoto')
   
    
    
    
]