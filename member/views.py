from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
# Create your views here.
def member(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def product(request):
    template = loader.get_template('product.html')
    return HttpResponse(template.render())

def krishna(request):
    template = loader.get_template('krishna.html')
    return HttpResponse(template.render())

def myfirst(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def game(request):
    template = loader.get_template('game.html')
    return HttpResponse(template.render())

def cou(request):
    template = loader.get_template('cou.html')
    return HttpResponse(template.render())



def navbar(request):
    template = loader.get_template('navbar.html')
    return HttpResponse(template.render())

def navbarhome(request):
    template = loader.get_template('navbarhome.html')
    return HttpResponse(template.render())

def navbarabout(request):
    template = loader.get_template('navbarabout.html')
    return HttpResponse(template.render())

def navbarcontact(request):
    template = loader.get_template('navbarcontact.html')
    return HttpResponse(template.render())

def navbarkrishna(request):
    template = loader.get_template('navbarkrishna.html')
    return HttpResponse(template.render())

def navbarproduct(request):
    template = loader.get_template('navbarproduct.html')
    return HttpResponse(template.render())

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        password = request.POST['password']
        user = authenticate(request,  email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'logged in successfully !')
            return redirect('home')
        else:
            messages.error(request,'Invaild email or password..')
    return render(request, 'login.html')

def reg(request):
    if request.method == 'POST':
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            #create neww user
            member.objects.create(username=username, email=email,password=password)
            messages.success(request,'account created succesfully..')
            return redirect('login')
    return render(request, 'login.html')
    
     
