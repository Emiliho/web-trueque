from django.conf.urls import url
from .views import *
from . import views

app_name = 'eleccion'

urlpatterns = [
	url(r'^$', listarCircunscripciones.as_view(), name='circunscripciones'),
	url(r'^crear/circunscripcion$', crearCircunscripcion.as_view(), name='crearCircunscripcion'),
	url(r'^editar/circunscripcion/(?P<pk>[0-9]+)/$', editarCircunscripcion.as_view(), name='editarCircunscripcion'),
	url(r'^circunscripcion/(?P<pk>[0-9]+)/$', views.listarMesas, name='mesas'),
	url(r'^circunscripcion/(?P<pk>[0-9]+)/crear/mesa$', views.crearMesa, name='crearMesa'),
	url(r'^mesa/(?P<pk>[0-9]+)/$', views.verMesa, name='verMesa'),
	url(r'^editar/mesa/(?P<pk>[0-9]+)/$', views.editarMesa, name='editarMesa'),
	url(r'^borrar/mesa/(?P<pk>[0-9]+)/$', views.borrarMesa, name='borrarMesa'),
	
	
	
	
]
