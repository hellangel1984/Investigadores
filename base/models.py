from django.db import models
from django.contrib import admin

# Create your models here.

class persona(models.Model):
    papellido = models.CharField(max_length=144)
    sapellido = models.CharField(max_length=144)
    nombre = models.CharField(max_length=144)
    email = models.EmailField(max_length=256)
    vivo = models.BooleanField()
    genero = models.ForeignKey('genero')
    def __unicode__(self):
        return '%s %s %s' % (self.papellido, self.sapellido, self.nombre)

class genero(models.Model):
    genero = models.CharField(max_length=38)
    genero2 = models.CharField(max_length=1)
    def __unicode__(self):
        return self.genero

class ubicacion(models.Model):
    estado = models.CharField(max_length=144)
    def __unicode__(self):
        return self.estado

#un investigador es una persona
class investigador(persona):
    nobilis = models.CharField(max_length=38)
    vigente = models.BooleanField()
    nivel = models.ForeignKey('nivel')
    area = models.ForeignKey('area')
    persona = persona
    ubicacion = models.ForeignKey('ubicacion')
    campo = models.ForeignKey('campo')
    especialidad = models.ForeignKey('especialidad')
    def __unicode__(self):
        return '%s %s %s %s' % (self.nobilis,self.nombre,self.sapellido, self.nombre)
    
class nivel(models.Model):
    nivel = models.CharField(max_length=38)
    nivel2 = models.CharField(max_length=1)
    def __unicode__(self):
        return self.nivel

class area(models.Model):
    area = models.CharField(max_length=144)
    area2 = models.CharField(max_length=1)
    def __unicode__(self):
        return self.area

class campo(models.Model):
    ncampo = models.CharField(max_length=144,blank=True,null=True)
    disciplina = models.ForeignKey('disciplina')

class disciplina(models.Model):
    ndisciplina = models.CharField(max_length=144,blank=True,null=True)
    sdisciplina = models.ForeignKey('sdisciplina')

class sdisciplina(models.Model):
    nsdisciplina = models.CharField(max_length=144,blank=True,null=True)


class especialidad(models.Model):
    nespecialidad = models.CharField(max_length=144)
    def __unicode__(self):
        return self.nespecialidad

#class adscripcion(models.Model):
#    adscripcion = models.CharField(max_length=144)
#    dependencia = models.ForeignKey('dependencia',blank=True, null=True)
#    def __unicode__(self):
#        return '%s %s' % (self.adscripcion,self.dependencia)

#class dependencia(models.Model):
#    nombre = models.CharField(max_length=144)
#    subdependencia = models.ForeignKey('self',blank=True, null=True)
#    def __unicode__(self):
#        return self.nnombre


admin.site.register(persona)
admin.site.register(investigador)
admin.site.register(genero)
admin.site.register(ubicacion)
admin.site.register(nivel)
admin.site.register(area)
admin.site.register(campo)
admin.site.register(disciplina)
admin.site.register(sdisciplina)
admin.site.register(especialidad)
#admin.site.register(adscripcion)
#admin.site.register(dependencia)
