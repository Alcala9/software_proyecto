from django.urls import path
from datos import views

urlpatterns = [
    path('', views.lista_datos, name='datos_lista'),
    path('nuevo', views.nuevo_datos, name='datos_nuevo'),
    path('eliminar/<int:id>', views.eliminar_datos, name='eliminar_datos'),
    path('editar/<int:id>', views.editar_datos, name='editar_datos'),
]
