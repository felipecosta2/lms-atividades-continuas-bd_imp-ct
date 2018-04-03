from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def contato(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print('Acesso via POST')

def login(request):
    if request.method == 'GET':
        
        print(“Acesso via GET”)
       

    else:
        request.POST.get("loginUser")
        request.POST.get("senhaUser")
        print(“Acesso via POST”)
        print("Acesso via POST com usuário", request.POST.get("loginUser"), "e senha", request.POST.get("senhaUser"))
    return render(request, 'login.html') 
    



