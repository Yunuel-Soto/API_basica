from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from Logica import manejo

def index(Request):
    response = {
        "status":"sucessfull",
        "code":200,
        "data": manejo.valor()
    }
    return  JsonResponse({"test": manejo.valor()})