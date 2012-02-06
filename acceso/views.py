# Create your views here.
from siieb.base.models import *
from siieb.acceso.models import *
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth


def index(request):
    return direct_to_template(request,template='acceso/entrar.html')

@csrf_exempt
def validaCredenciales(request):
    #response = HttpResponse()
    #response['Content-Type'] = "text/javascript"
    try:
        u = siiebUser.objects.get(username__exact = request.POST['usuario'])
        if u.password == request.POST['password']:
            #return direct_to_template('request','/siieb/busqueda/')
            #return HttpResponseRedirect('/siieb/busqueda/')
            mensaje = { 'mensaje':'Credenciales validas','acceso':0}
            return render_to_response('acceso/resultados.html', mensaje ,context_instance = RequestContext(request))
        else:
            mensaje = { 'mensaje':'Usuario y/o password incorrectos','acceso':1}
            return render_to_response('acceso/resultados.html', mensaje ,context_instance = RequestContext(request))
    except:
        mensaje = { 'mensaje':'Usuario y/o password incorrectos','acceso':1}
        return render_to_response('acceso/resultados.html' , mensaje ,context_instance = RequestContext(request))
    

@csrf_exempt
def entra(request):
#    print request.POST['usuario']
#    print request.POST['password']
    try:
        return HttpResponseRedirect('/siieb/busqueda/')
    except:
        print 'Except :('
        return HttpResponseRedirect('/siieb/index/')
