from django import forms

from cadastros.models import Cidade, Estado, Pais


class CidadeForm(forms.ModelForm):

    class Meta:
        model = Cidade
        fields = '__all__'

    def clean(self):

        nome = self.cleaned_data['nome']

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = '__all__'

    def clean(self):
        nome = self.cleaned_data['nome']

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

    def clean(self):
        nome = self.cleaned_data['nome']