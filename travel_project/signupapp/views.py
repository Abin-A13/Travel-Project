from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        usnr = request.POST['username']
        pasn = request.POST['password']
        user = auth.authenticate(username=usnr, password=pasn)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request, "login1.html")


def Register(request):
    if request.method == 'POST':
        usr = request.POST["username"]
        fn = request.POST['frist_name']
        ln = request.POST['last_name']
        eml = request.POST['mail']
        pas = request.POST['password1']
        cnpas = request.POST['password2']
        if pas == cnpas:
            if User.objects.filter(username=usr).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            elif User.objects.filter(email=eml).exists():
                messages.info(request, "Email already exist ")
                return redirect('register')
            else:
                user = User.objects.create_user(username=usr, first_name=fn, last_name=ln, email=eml, password=pas)
                user.save()
                print('data saved')
                return redirect("login")

        else:
            messages.info(request, "password not match")
            return redirect("register")
        return redirect('/')
    return render(request, "signup.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

