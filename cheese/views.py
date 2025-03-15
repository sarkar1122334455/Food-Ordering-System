from django.shortcuts import render,redirect
from django.http import HttpResponse
from cheese.models import *
# Create your views here.

def about(request):
    return render(request, 'about.html' )
def book(request):
    return render(request, 'book.html' )
def burger(request):
    return render(request, 'burger.html' )

def menu(request):
    return render(request, 'menu.html' )
def login(request):
    return render(request, 'login.html' )
def registration(request):
    return render(request, 'registration.html' )
def reg(request):
    u=ecom()
    u.fullname=request.GET['fullname' ]   
    u.username=request.GET['username']      
    u.email=request.GET['email']      
    u.password=request.GET['password']   
    u.save()
    return render(request,'login.html')
def log(request):
    a=request.GET['username']
    b=request.GET['password']
    if ecom.objects.filter(username=a, password=b):
        return render(request, 'burger.html')
    else:
        return render(request, 'login.html')
    

def show(request):
    a=ecom.objects.all()
    return render(request,'show.html',{'x':a})
def dele(request,id):
    d=ecom.objects.get(id=id)
    d.delete()
    return redirect("../show")
def edit(request,id):
    d=ecom.objects.get(id=id)
    return render(request,'edit.html',{'x':d})
def edcode(request,id):
    d=ecom.objects.get(id=id)
    d.fullname=request.GET['fullname']   
    d.username=request.GET['username']      
    d.email=request.GET['email']      
    d.password=request.GET['password'] 
    d.save()
    return redirect('../show')

def logout(request):
    return render(request, 'logout.html' )


def ind(request):
    u=call()
    u.name=request.GET['name']   
    u.phno=request.GET['phno']      
    u.email=request.GET['email']        
    u.cal=request.GET['cal']   
    u.save()
    return render(request,'burger.html')