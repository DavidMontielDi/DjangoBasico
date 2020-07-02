from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context

# Create your views here.


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido=apellido

def hello(request,nombre,apellido):
    p1=Persona(nombre,apellido)
    ahora = datetime.datetime.now()
    doc_externo = open("C:/Users/David/Documents/Django/mysite/inicio/plantillas/hola.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido,"momento_actual":ahora})
    document=plt.render(ctx)
    return HttpResponse(document)

def adios(request):
    document = """  <html>
                        <body> 
                            <h1>Adios!</h1> 
                        </body>
                    </html>"""
    return HttpResponse(document)    

def dame_fecha(request):
    fecha_actual=datetime.datetime.now()
    document = """  <html>
                        <body> 
                            <h1>Hora y fecha actual %s</h1> 
                        </body>
                    </html>""" %fecha_actual    
    return HttpResponse(document)  

def calculaEdad(request,edad, anio):
    
    periodo=anio-2020
    edadFutura=edad+periodo
    document = """  <html>
                        <body> 
                            <h1>En el año %s tendras %s años </h1> 
                        </body>
                    </html>""" %(anio,edadFutura)
    return HttpResponse(document)  
     