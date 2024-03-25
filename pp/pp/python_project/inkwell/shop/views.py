from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm,OwnerRegistrationForm
from django.http import JsonResponse
from .models import Owner, Product, Category
def Home(request):
    categories = Category.objects.first()
    return render(request,"index.html",{'category': categories })


def login_view(request):
    return render(request , "login.html")

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def owner_registration_view(request):
    if request.method == 'POST':
        form = OwnerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            matching_customer = User.objects.filter(username=form.username).first()
            if matching_customer:
                matching_customer.isOwner = True
                matching_customer.save()

            return redirect('/home')
    else:
        form = OwnerRegistrationForm()

    return render(request, 'owner.html', {'form': form})

def add_product(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        quantity = request.POST.get('quantity')

        owner = request.POST.get('owner')
        owner_object = Owner.objects.get(first_name = owner)

        product = Product.objects.create(
            name=name,
            price=price,
            category_id=category_id,
            description=description,
            image=image,
            owner=owner_object,  
            quantity=quantity,
        )
        return redirect('show_product')


    categories = Category.objects.all()
   
    return render(request, 'product.html', {'categories': categories })

def show_product(request):
    products = Product.objects.all()
    return render(request, 'product_show.html', {'products': products})

def product_details(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    return render(request, 'product_inspection.html', {'product': product})


def catname(request, cat_name):
    category = get_object_or_404(Category, name=cat_name)
    products = Product.objects.filter(category=category)

    return render(request, 'product_show.html', {'products': products})
   

def search_owner(request):
    if request.method == 'GET':

        search = request.GET.get('search')

        owner_object = Owner.objects.get(first_name = search)
        owner_products = Product.objects.filter(owner__first_name=search)

    return render(request, 'search_result.html', {'owner':owner_object,'owner_products':owner_products })

def product_suggestions(request):
    if request.method == 'GET' and 'search' in request.GET:
        search_term = request.GET.get('search')
        products = Product.objects.filter(name__icontains=search_term)[:5]
        suggestions = [product.name for product in products]
        return JsonResponse({'suggestions': suggestions})
    else:
        return JsonResponse({}) 