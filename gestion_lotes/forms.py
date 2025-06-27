from django import forms
from .models import Lote

class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = ['nombre_archivo', 'archivo']