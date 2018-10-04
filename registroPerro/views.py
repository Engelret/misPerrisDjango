from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html',{'nombre':"oso"})

def registroPerro(request):
    return render(request,'formulario.html',{})

def registrado(request):
    nombre = request.POST.get('nombre','')
    raza = request.POST.get('raza','')
    descripcion = request.POST.get('descripcion','')
    estado = request.POST.get('estado','')
    foto = request.POST.get('foto','')
    return HttpResponse('nombre :'+nombre+" raza : "+raza+" descripcion : "+descripcion+" estado : "+estado+ " foto : "+foto)

