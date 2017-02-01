from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test


class listarCircunscripciones(View):
	template_name = 'eleccion/circunscripciones.html'

	def get(self, request, *args, **kwargs):
		circunscripciones = Circunscripcion.objects.all()
		return render(request, self.template_name, {'circunscripciones': circunscripciones})

class crearCircunscripcion(View):
	form_class = FormularioCircunscripcion
	template_name = 'eleccion/crearCircunscripcion.html'
 
	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		formulario = self.form_class()
		return render(request, self.template_name, {'formulario': formulario})

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		formulario = self.form_class(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return redirect('circunscripciones')
		return render(request, self.template_name, {'formulario': formulario})


class editarCircunscripcion(View):
	form_class = FormularioCircunscripcion
	template_name = 'eleccion/editarCircunscripcion.html'

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		formulario = self.form_class()
		circunscripcion = Circunscripcion.objects.get(pk=self.kwargs.get('pk'))
		return render(request, self.template_name, {'formulario': formulario, 'circunscripcion': circunscripcion})

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		formulario = self.form_class(request.POST, request.FILES)
		if formulario.is_valid():
			circunscripcion = Circunscripcion.objects.get(nombre=self.kwargs.get('nombre'))
			circunscripcion.escanos = request.POST['escanos']
			circunscripcion.nombre = request.POST['nombre']
			circunscripcion.save()
			return redirect('/')
		return render(request, self.template_name, {'formulario': formulario})

def listarMesas(request, pk):
	circunscripcion = get_object_or_404(Circunscripcion, pk=pk)
	mesas = circunscripcion.mesa.set_all()
	return render(request, 'eleccion/mesas.html', {'circunscripcion': circunscripcion, 'mesas': mesas})


def verMesa(request, pk):
	mesa = get_object_or_404(Mesa, pk=pk)
	return render(request, 'verMesa.html', {'mesa': mesa})


@login_required
def crearMesa(request, pk):
	circunscripcion = get_object_or_404(Cirscunscripcion, pk=pk)
	if request.method == 'POST':
		formulario = FormularioMesa(request.POST)
		if formulario.is_valid():
			mesa = formulario.save(commit=False)
			mesa.circunscripcion = circunscripcion
			mesa.save()
			return redirect('verCircunscripcion', pk=circunscripcion.pk)
	else:
		formulario = FormularioMesa()
	return render(request, 'crearMesa.html', {'formulario': formulario})


@login_required
def editarMesa(request, pk):
	mesa = get_object_or_404(Mesa, pk=pk)
	if request.method == 'POST':
		formulario = FormularioMesa(request.POST, instance=mesa)
		if formulario.is_valid():
			mesa.save()
			return redirect('verMesa', pk=circunscripcion.pk)
	else:
		formulario = FormularioMesa(instance=mesa)
	return render(request, 'editarMesa.html', {'formulario': formulario})


@login_required
def borrarMesa(request, pk):
	mesa = get_object_or_404(Mesa, pk=pk)
	circunscripcion = mesa.circunscripcion
	mesa.delete()
	return redirect('verCircunscripcion', pk=circunscripcion.pk)







def asignacion(request, nombre):
	votos = []
	circunscripcion = Circunscripcion.objects.get(nombre=nombre)
	for x in range(2):
		maxPartido = ""
		maxVotos = 0
		for partido in Partido.objects.all():
			if not partido.nombre in votos:
				total = 0
				for mesa in circunscripcion.mesa_set.all():
					for resultado in mesa.resultado_set.all():
						if resultado.partido == partido:
							total += resultado.votos
				if total > maxVotos:
					maxVotos = total
					maxPartido = partido.nombre
		votos.append(maxPartido)
	votos.insert(1, circunscripcion.escanos -1)
	votos.insert(3, 1)
	return render(request, 'asignaciones.html', {'circunscripcion': circunscripcion, 'votos': votos})

def userLogin(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid():
			user = request.POST['username']
			passwd = request.POST['password']
			access = authenticate(username=user, password=passwd)
			if access is not None:
				if access.is_active:
					login(request, access)
					return redirect('/')
				else:
					return render(request, 'inactive.html')
			else:
				return render(request, 'nouser.html')
	else:
		formulario = AuthenticationForm()
	context = {'formulario': formulario}
	return render(request, 'login.html', context)

@login_required(login_url='/login')
def userLogout(request):
	logout(request)
	return redirect('/')













