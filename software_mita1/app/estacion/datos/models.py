from django.db import models




# Video 2 

ESTACIONES =[ 
    ("1", "Estacion meteorologica 1 Ojocaliente "),

]

PROCEDENCIA =[ 
    ("1", "Universidad Autonoma de Zacatecas"),
    ("2", "Sector privado"),
    ("3", "Sector publico"),
]

class Usuarios(models.Model):
    nombre      = models.CharField(max_length=100)
    clave       = models.CharField(max_length=100)
    procedencia = models.TextField("Procedencia", max_length=1, choices=PROCEDENCIA)
    estacion    = models.TextField("Estacion", max_length=1, choices=ESTACIONES)

 
    def __str__(self):
        return self.nombre
    
#class Variables(models.Model):
#
#
#   def __str__(self):
#        return self.nombre