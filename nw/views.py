from django.shortcuts import render,HttpResponse

#from django.http import HttpResponse
def index(request):
    return HttpResponse("hello world")

def hi(request):
    return render(request,"index.html")
def picture (request):
    return render(request,"image.html")

def log(request):
    return render(request,"login.html")