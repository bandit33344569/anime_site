from django.shortcuts import render
from django.http import HttpResponse


def index(requets):
    print(requets)
    return HttpResponse('hello word')

def test(request):
    return  HttpResponse('<h1>test</h1>')