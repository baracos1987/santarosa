from django.urls import path, include
from .views import home

#creamos la URL para llamar funcion home en la vista views
urlpatterns = [
    path('', home, name="home"),

]