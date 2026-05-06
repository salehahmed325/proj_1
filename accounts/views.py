from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print("username already taken")
                messages.info(request, "username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("email already taken")
                messages.info(request, "email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                messages.info(request, f"user {username} created!")
                user.save()
        else:
            print("password not matched")
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')