



# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.http import JsonResponse
from django.db import IntegrityError
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login
from .models import *
import json



def reg(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                return render(request, 'core/index.html', {'form': form, 'success_message': "User registered successfully."})
            except IntegrityError:
                form.add_error('username', 'Username already exists. Please choose a different one.')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/reg.html', {'form': form})
def loginpage(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to a home page or any other page
    else:
        form = UserLoginForm()
    return render(request, 'core/userlog.html', {'form': form})

def index(request):
  

    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'core/index.html',context)
def store(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'core/store.html', context)
def store2(request):
    productsdark = Productdark.objects.all()
    context={'productsdark':productsdark}
    return render(request, 'C:/Users/harik/OneDrive/Desktop/Django/core/store2.html', context)
def store3(request):
    productstan = Producttan.objects.all()
    context={'productstan':productstan}
    return render(request, 'core/store3.html', context)
def store4(request):
    productsage = Productage.objects.all()
    context={'productsage':productsage}
    return render(request, 'core/store4.html', context)
def store5(request):
    productsagehair = Productagehair.objects.all()
    context={'productsagehair':productsagehair}
    return render(request, 'core/store5.html', context)
def store6(request):
    productsdan = Productdan.objects.all()
    context={'productsdan':productsdan}
    return render(request, 'core/store6.html', context)

def store7(request):
    productsfri = Productfri.objects.all()
    context={'productsfri':productsfri}
    return render(request, 'core/store7.html', context)
def perfumes(request):
    productsperfumes = Productperfumes.objects.all()
    context={'productsperfumes':productsperfumes}
    return render(request, 'core/perfumes.html', context)
def bathandbody(request):
    productsbath = Productbath.objects.all()
    context={'productsbath':productsbath}
    return render(request, 'core/bathandbody.html', context)
def skincare(request):
    return render(request, 'core/skincare.html')
def image(request):
    return render(request, 'static/image')
def knownskin(request):
    return render(request, 'core/knownskin.html')
def unknownskin(request):
    return render(request, 'core/unknownskin.html')
def knownhair(request):
    return render(request, 'core/knownhair.html')
def acne(request):
    return render(request, 'core/acne.html')
def darkspot(request):
    return render(request, 'core/darkspot.html')
def tan(request):
    return render(request, 'core/tan.html')
def aging(request):
    return render(request, 'core/aging.html')

def blog(request):
    return render(request, 'core/blog.html')
def prodesc6(request):
    return render(request, 'core/prodesc6.html')

def skintype(request):
    return render(request, 'core/skintype.html')
def product_detail(request,slug,id):
    return render(request, 'category_pro')