from django.urls import path
from webpage import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('nosotros', views.nosotros, name="Nosotros"),
    path('servicios', views.servicios, name="Servicios"),
    path('portafolio', views.portafolio, name="Portafolio"),
    path('contacto', views.contacto, name="Contacto"),
]