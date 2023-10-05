from django.shortcuts import render, HttpResponse

def posts(request):
    return HttpResponse('<h1>Pagina de publicaciones</h1>')

def post(request, id):
    return HttpResponse('<h1>pagina de blog</h1>')

# Create your views here.
