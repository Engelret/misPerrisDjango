from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('registroPerro/',views.registroPerro, name="registroPerro")
    path('registro/registrado',views.registrado = name="registrado")
]