from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def signup(request):

    if request.method == "POST":
        
        username1 = request.POST["username"]
        email1 = request.POST["email"]
        password = request.POST["password"]
        password1 = request.POST["password1"]

        if password == password1:

            if User.objects.filter(email = email1).exists():
                messages.info(request,"Email already exists")
                return redirect("signup")
            elif User.objects.filter(username = username1).exists():
                messages.info(request,"USername already exists")
                return redirect("signup")
            else:
                user= User.objects.create_user(username=username1,email=email1,password=password)
                user.save()
                return redirect("login")
        
        else:
            messages.info(request," Password not the same")
            return redirect("signup")
    
    else:
        return render(request, "pages/signup.html")