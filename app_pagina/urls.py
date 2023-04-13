from django.urls import path, include
from .views import home, dashboard, educacion, patrulleritos, tramites

#creamos la URL para llamar funcion home en la vista views
urlpatterns = [
    path('', home, name="home"),
    path('dashboard',dashboard, name="dashboard"),
    path('educacion',educacion,name="educacion" ),
    path('patrulleritos',patrulleritos,name='patrulleritos'),
    path('tramites', tramites,name='tramites'),

]