from django import forms
from .models import *
from django.contrib.auth.models import User

class FormularioCircunscripcion(forms.ModelForm):

	class Meta:
		model = Circunscripcion
		fields = ('nombre', 'escanos',)

class FormularioMesa(forms.ModelForm):

	class Meta:
		model = Mesa
		fields = ('nombre',)

class FormularioResultado(forms.ModelForm):

	class Meta:
		model = Resultado
		fields = ('partido', 'mesa', 'votos',)

class FormularioUsuario(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password']
