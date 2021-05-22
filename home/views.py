
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    products = Product.objects.all().order_by('-instant')
    context = {'products': products}
    return render(request, "home.html", context)


def search(request):
    if request.method == 'POST':
        key = request.POST['key']

        in_title = Product.objects.filter(p_name__icontains=key)
        in_desc = Product.objects.filter(p_desc__icontains=key)

        results = in_title.union(in_desc)

        context = {'results': results, 'key': key}

        if results.count() == 0:
            return render(request, 'search2.html', context)

        else:
            return render(request, 'search1.html', context)


def product(request, p_id):
    product = Product.objects.get(p_id=p_id)
    context = {'product': product}
    return render(request, 'product.html', context)


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'username already exists please login')
            return redirect('home')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists please login')
            return redirect('home')

        else:
            if password1 == password2:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                user.save()
                messages.info(request, 'account created for' + username)
                return redirect('home')
            else:
                messages.info(request, 'password not matching')
                return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect("home")


def logout_user(request):
    logout(request)
    return redirect('home')


def placeOrder(request, p_id, buyer_id):
    if request.method == 'POST':
        user = User.objects.get(id=buyer_id)
        p_id=request.POST['p_id']
        area=request.POST['area']
        city=request.POST['city']
        pin=request.POST['pin']
        phone=request.POST['phone']
        email=user.email
        buyer=user.username
        newOrder=Orders(p_id=p_id,area=area,city=city,phone=phone,email=email,pin=pin,buyer=buyer)
        newOrder.save()

        order_id=newOrder.order_id

        params_dict = {
        "MID": "mid",
        "ORDER_ID": "order_id",
        "CUST_ID": "cust_id",
        "TXN_AMOUNT": "1",
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "http://127.0.0.1:8000/"+p_id+'/'+buyer_id+'/'
    }

    else:
        context = {'p_id': p_id, 'buyer_id': buyer_id}
        return render(request, 'address.html', context)

@csrf_exempt
def payment(request):
    pass