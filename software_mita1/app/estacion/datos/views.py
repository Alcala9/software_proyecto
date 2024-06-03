from django.shortcuts import render, redirect
from datos.models import Usuarios
from datos.forms import FormDato


# Create your views here.
def lista_datos(request):
    datos = Usuarios.objects.all()
    return render(request, 'datos.html', {'datos': datos})


def eliminar_datos(request, id):
    datos = Usuarios.objects.get(id=id)
    datos.delete()
    return redirect('datos_lista')

def nuevo_datos(request):
    if request.method == 'POST':
        form = FormDato(request.POST)
        if form.is_valid():
            form.save()
            return redirect('datos_lista')

    else:
        form = FormDato()
    return render(request, 'nuevo_datos.html',{'form':form})

def editar_datos (request, id):
    datos = Usuarios.objects.get(id=id)

    if request.method == 'POST':
        form = FormDato(request.POST, instance=datos)
        if form.is_valid():
            form.save()
            return redirect('datos_lista')

    else:
        form = FormDato(instance=datos)
    return render(request, 'editar_datos.html',{'form':form})