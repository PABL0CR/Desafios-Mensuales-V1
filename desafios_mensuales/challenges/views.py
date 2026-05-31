from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

desafios_mensuales = {
    "enero": "Haz 10 minutos de meditación cada día.",
    "febrero": "Camina al menos 5.000 pasos diarios.",
    "marzo": "Aprende una palabra nueva en inglés cada día.",
    "abril": "Escribe un diario con 3 cosas positivas cada noche.",
    "mayo": "Dedica 20 minutos a leer un libro cada día.",
    "junio": "Haz 15 minutos de ejercicio físico diario.",
    "julio": "Prueba una receta nueva cada semana.",
    "agosto": "Dedica tiempo a un hobby creativo (dibujar, música, etc.).",
    "septiembre": "Haz una limpieza digital: organiza tus archivos y correos.",
    "octubre": "Aprende algo nuevo sobre programación cada semana.",
    "noviembre": "Haz un acto de bondad al azar cada día.",
    "diciembre": "Reflexiona sobre tus logros del año y fija metas nuevas."
}

# Create your views here.

def index(request):
    list_items = ""
    meses = list(desafios_mensuales.keys())

    for mes in meses:
        mayus_mes = mes.capitalize()
        mes_path = reverse("mensual", args=[mes])
        list_items += f"<li><a href=\"{mes_path}\">{mayus_mes}</a></li>"

    # "<li><a href="...">Enero</a></li><li><a href ="...">Febrero</a></li>..."
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
    

def desafio_mensual_por_numero(request, mes):
    meses = list(desafios_mensuales.keys())

    if mes > len(meses):
        return HttpResponseNotFound("<h1>Mes invalido</h1>")
        
    redireccion_mes = meses[mes-1]
    redireccion_path = reverse("mensual", args=[redireccion_mes]) #/challenge/enero
    return HttpResponseRedirect(redireccion_path)

def desafio_mensual(request, mes):
    try:
        challenge_text = desafios_mensuales[mes]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>No se pudo encontrar</h1>")