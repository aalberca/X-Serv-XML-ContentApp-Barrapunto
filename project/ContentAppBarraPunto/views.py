from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from ContentAppBarraPunto.barrapunto import obtener_noticias

# Create your views here.

def pagina(request, identificador):

    try:
        pag = Pages.objects.get(id = int(identificador))
        respuesta = pag.page
        noticias = obtener_noticias()
        respuesta += "<br/>" + "<h1>Estas son las noticias obtenidas de BarraPunto</h1><br/>" + noticias
    except Pages.DoesNotExist:
        respuesta = "No existe ese nombre con contenidos en la base de datos"
    return HttpResponse(respuesta)

def muestra_todo(request):
    lista = Pages.objects.all()
    respuesta = "<ol>"
    for pag in lista:
        respuesta += '<li><a href="' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)
