from django import forms
from datos.models import Usuarios

class FormDato(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = '__all__'
        