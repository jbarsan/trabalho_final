from django import forms
from .models import Receita, Comentario


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ('titulo', 'tempo_preparo', 'rendimento', 'ingredientes', 'modo_preparo',)


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('autor', 'comentario',)
