from django import forms
from evaluacion2b.models import Proyecto

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
