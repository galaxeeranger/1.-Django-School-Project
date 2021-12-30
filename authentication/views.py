from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        auth_user = User.objects.create_user(username,email)
        auth_user.pass1 = pass1
        auth_user.phone = phone


        auth_user.save()

        messages.success(request, "Your Account has been Successfully Created.")


        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == 'POST':
        email = request.POST["email"]
        pass1 = request.POST["pass1"]

        user = authenticate(email=email,pass1=pass1)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "authentication/index.html", {'username':username})
        
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.successs(request, "Logged Out Successfully!")
    return redirect('home')