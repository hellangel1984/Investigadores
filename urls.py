from django.conf.urls.defaults import patterns, include, url
from siieb.buscador.views import *
from siieb.acceso.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siieb.views.home', name='home'),
    # url(r'^siieb/', include('siieb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^siieb/busqueda/$',busqueda),
    url(r'^siieb/buscaNombre/$',buscaNombre),
    url(r'^siieb/valida1/$',valida1),
    url(r'^siieb/login/$',validaCredenciales),
    url(r'^siieb/index/$',index),
    url(r'^siieb/entra/$',entra),
)
