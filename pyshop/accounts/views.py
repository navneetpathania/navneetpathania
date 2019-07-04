from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        if password == confirm:

            if User.objects.filter(username=username).exists():
                messages.info(request,"user name not available")
                return redirect("/register")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email name not available")
                return redirect("/register")
            else:
                user = User.objects.create_user(username=username,password=password,
                                                email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
                return redirect("/register/login")
        else:
            messages.info(request, "password not match")
            return redirect("/register")

    else:
        return render(request,"accounts/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"wrong detailes")
            return redirect('/login')

    else:
        return render(request,"accounts/login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")