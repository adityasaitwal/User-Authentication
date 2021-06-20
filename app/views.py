from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import SignUpForm

# Create your views here.

def Home(request):
    return render(request,"home.html")

def SignUp(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(SignUpDone)
    else:
        form = SignUpForm()
    return render(request,"signup.html",{"form":form})

def SignUpDone(request):
    return HttpResponse("Welcome!, Your account is created")
    
