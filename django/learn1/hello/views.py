from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    return render(request, "hello/index.html")
    # untuk penamaan dir nya, wajib diperhatikan

def al(request) :
    return HttpResponse("hello Al!")

def abi(request) :
    return HttpResponse("hello abi")

def sapa(request, name:str) :
    return render(request, "hello/greet.html", {
        "name" : name.capitalize()
    })
    # context dalam render() itu dapat menyimpan variable untuk html
    # nama pada dict digunakan untuk variable pada html
    # key pada dict digunakan untuk menyimpan argument kita