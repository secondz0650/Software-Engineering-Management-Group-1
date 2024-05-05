from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import Product
from django.contrib.auth import logout as auth_logout


def land(request):
    return render(request, 'Landing_PAGE.html')


def SignUP_Form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm = request.POST.get('pass2')

        if len(password) < 8 and len(password)== 8:
            messages.warning(request, "Password must be at least 8 characters long.")
            return redirect('/SignUP_Form')

        if password != confirm:
            messages.warning(request, "password does not match")
            return redirect('/SignUP_Form')
        
        try:
            if User.objects.get(username=username):
                messages.info(request, 'username is taken')
                return redirect('/SignUP_Form')
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request, 'email is taken')
                return redirect('/SignUP_Form')
        except:
            pass

        
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.info(request, 'signup success')
        return redirect('/Login_Form')
    return render(request, 'SignUP_Form.html')


def homepage(request):
    return render(request, 'homepage.html')


def Login_Form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        
        myuser = authenticate(username=username, password=password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, 'login successful')
            return redirect('/homepage')
        else:
            messages.error(request, 'Login unsuccessful')
            return redirect('/Login_Form')
    return render(request, 'Login_Form.html' )


def about(request):
    return render(request, 'about.html')


def product(request):
    return render(request, 'product.html')


def blog(request):
    return render(request, 'blog.html')

def vegetable(request):
    return render(request, 'vegetable.html')

def fruit(request):
    return render(request, 'fruit.html')


def contactus(request):
    return render(request, 'contactus.html')

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Product.objects.filter(name__icontains=query)
            return render(request, 'searchbarNew.html', {'products':products})
        else:
            print("No information to show")
            return render(request, 'searchbarNew.html', {})
def my_logout(request):
    auth_logout(request)
    messages.info(request, 'Logout success')
    return redirect('/')






