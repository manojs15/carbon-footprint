# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def login(request):
    return render(request,"login.html")


def guest(request):
    return render(request,"calc.html")
def register(request): 
    return render(request,"register.html")

def signup(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        emaill=request.POST.get('email')
        passw=request.POST.get('password')
        my_user=User.objects.create_user(uname,emaill,passw)
        my_user.save()
        return redirect('login')
    
def log(request):
      if request.method == 'POST':
          username = request.POST.get('usern')
          pass1 = request.POST.get('passn')
          user=authenticate(request,username=username,password=pass1)
          if user is not None:
              login(request)
              return redirect('main')
          else:
              return HttpResponse("u r wrong")
      return render(request, 'login.html')



def main(request):
    return render(request,"main.html")
def cacal(request):
    return render(request,"calculator.html")
def recommand(request):
    return render(request,"personalreccomnedation.html")
def social(request):
    return render(request,"socialconnectvity.html")
def edu(request):
    return render(request,"eduhub.html")
def gol(request):
    return render(request,"goal.html")
def copi(request):
    return render(request,"aicopilot.html")
def grap(request):
    return render(request,"graph.html")
def nxtmth(request):
    return render(request,"nextmonth.html")
def led(request):
    return render(request,"lead.html")

def det(request):
    return render(request,"det.html")
def quiz(request):
    return render(request,"quiz.html")
def research(request):
    return render(request,"research.html")

def profile(request):
    return render(request,"social.html")


