# Create your views here.
from siieb.base.models import *
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

def busqueda(request):
    return direct_to_template(request,template='buscador/busqueda.html')

@csrf_exempt
def buscaNombre(request):
    #print request.POST
    if request.POST['nombre'] and request.POST['papellido'] and request.POST['sapellido']:
        resultados = investigador.objects.filter(nombre__icontains = request.POST['nombre'],papellido__icontains = request.POST['papellido'],sapellido__icontains = request.POST['sapellido'])
    elif request.POST['sapellido']:
        resultados = investigador.objects.filter(sapellido__icontains = request.POST['sapellido'])
    elif request.POST['papellido']:
        resultados = investigador.objects.filter(papellido__icontains = request.POST['papellido'])
    elif request.POST['nombre']:
        resultados = investigador.objects.filter(nombre__icontains = request.POST['nombre'])
    else:
        resultados = investigador.objects.filter(nombre__icontains = '@')
    return render_to_response('buscador/resultados.html', {'resultados':resultados}, context_instance = RequestContext(request))


@csrf_exempt
def valida1(request):
    #print request.POST
    #if request.POST['nombre'].isdigit():
    if request.POST['nombre'].isdigit():
        mvalida = { 'mensaje':'mal no uses numeros'}
    else:
        mvalida = { 'mensaje':'nada'}
    return render_to_response('buscador/valida.html', mvalida, context_instance = RequestContext(request))


