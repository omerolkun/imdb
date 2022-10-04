from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import UserForm
from django.http import HttpResponse,HttpResponseRedirect

def home(request):
	return render(request, 'home.html' )


def yazboz(request):
    context = { 'iteration':range(1,39)}
    return render(request, 'yazboz.html', context)

def signup(request):
    print( "reodiasfd,", request.method) 
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        print("ioersa")
        if form.is_valid():
            print("form is valid")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
        print("elsoooo")
    
    return render(request, 'signup.html', {'form':form})

