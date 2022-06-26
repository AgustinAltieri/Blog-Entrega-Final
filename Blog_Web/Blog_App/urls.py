from django.urls import path

from Blog_App import views

urlpatterns = [

    path('', views.base, name="Base"),
    path('inicio', views.inicio, name="Inicio"),
    path('mundo', views.mundo, name="Mundo"),
    path('gastronomía', views.gastronomía, name="Gastronomía"),
    path('recetas', views.recetas, name="Recetas"),
    path('mensajes', views.mensajes, name="Mensajes"),
]