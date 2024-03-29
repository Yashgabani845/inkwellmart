from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm,OwnerRegistrationForm
from django.http import JsonResponse
from .models import Cart, Owner, Product, Category,Order,Customer
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
        if username=="admin" and pass1=="admin":
            return render(request,'admin.html')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            request.session['username'] = user.username
            request.session['email'] = user.email
            request.session['first_name'] = user.first_name
            request.session.save() 
            return redirect('/home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    request.session.flush()
    return redirect('login')


def owner_registration_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('Username')
        sales = request.POST.get('sales')
        gst_no = request.POST.get('gst_no')
        ownerkey = request.POST.get('ownerkey')

        owner = Owner(first_name=first_name, sales=sales, gst_no=gst_no, ownerkey=ownerkey)
        owner.save()
        return redirect('owner_verification')  

    return render(request, 'owner.html')


def owner_verification_view(request):
    if request.method == 'POST':
        ownerkey = request.POST.get('ownerkey')
        owner = request.session.get('username')  
        logged_in_owner=Owner.objects.get(first_name = owner)
        if logged_in_owner and logged_in_owner.ownerkey == ownerkey:
            return redirect('owner_side') 
        else:
            return render(request, 'varification.html', {'error': 'Invalid owner key'})
    else:
        return render(request, 'varification.html')

from django.shortcuts import render
from .models import Owner, Product

def owner_side(request):
    owner_username = request.session.get('username')
    
    owner_data = Owner.objects.get(first_name=owner_username)
    owner_products = Product.objects.filter(owner=owner_data)
    return render(request, 'owner_side.html', {'owner_data': owner_data, 'owner_products': owner_products})


def checking_owner(request):
    username = request.session.get('username')
    existing_owner = Owner.objects.filter(first_name=username).exists()
    
    if existing_owner:
        return redirect('owner_verification')
    else:
        return redirect('owner_registration')
    

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
        owner_username = request.session.get('username')
    
        owner_data = Owner.objects.get(first_name=owner_username)
        owner_products = Product.objects.filter(owner=owner_data)
        return render(request, 'owner_side.html', {'owner_data': owner_data, 'owner_products': owner_products})

    categories = Category.objects.all()
    return render(request, 'product.html', {'categories': categories })



def buy_now(request,product_name):
    product=Product.objects.get(name = product_name)
    user=Customer.objects.get(username=request.session.get('username'))
    orders=Order.objects.create(
    product=product,
    owner=product.owner,
    customer=user,
    quantity=1,
    status=True
    )
    order = Order.objects.filter(customer = user)
    return render(request, 'order.html', {'orders': order })


    

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
        print(search_term)
        products = Product.objects.filter(name__icontains=search_term)[:10]
        suggestions = [product.name for product in products]
        return JsonResponse({'suggestions': suggestions})
    else:
        return JsonResponse({}) 
    
def profile(request):
    username = request.session.get('username')
    email = request.session.get('email')
    first_name = request.session.get('first_name')
    return render(request, 'profile.html', {'username': username, 'email': email, 'first_name': first_name})

from django.shortcuts import redirect, get_object_or_404
from .models import Cart, Product

def add_to_cart(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    username = request.session.get('username')
    
    existing_cart_item = Cart.objects.filter(product=product, username=username).first()
    if existing_cart_item:
        existing_cart_item.quantity_cart += 1
        existing_cart_item.save()
    else:
        cart_item = Cart(product=product, username=username)
        cart_item.save()

    return redirect('cart')

def remove_from_cart(request, product_name):
    username = request.session.get('username')
    product = get_object_or_404(Product, name=product_name)
    cart_item = get_object_or_404(Cart, product=product, username=username)
    cart_item.delete()
    return redirect('cart')

def increase_quantity(request, product_name):
    username = request.session.get('username')
    product = get_object_or_404(Product, name=product_name)
    cart_item = get_object_or_404(Cart, product=product, username=username)
    cart_item.quantity_cart += 1
    cart_item.save()
    return redirect('cart')

def decrease_quantity(request, product_name):
    username = request.session.get('username')
    product = get_object_or_404(Product, name=product_name)
    cart_item = get_object_or_404(Cart, product=product, username=username)
    if cart_item.quantity_cart > 1:
        cart_item.quantity_cart -= 1
        cart_item.save()
    return redirect('cart')


def cart(request):
    username = request.session.get('username')
    cart_items = Cart.objects.filter(username=username)
    
    total_price = sum(item.product.price * item.quantity_cart for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    
    return render(request, 'cart.html', context)


from django.contrib import messages

def buy_all(request):
    username = request.session.get('username')
    cart_items = Cart.objects.filter(username=username)
    user = Customer.objects.get(username=username)  

    for item in cart_items:
        product = item.product
        quantity_in_cart = item.quantity_cart

        if product.quantity < quantity_in_cart:
            continue 

        order = Order.objects.create(
            product=product,
            owner=product.owner,
            customer=user,  
            quantity=quantity_in_cart,
            status=True
        )
        product.quantity -= quantity_in_cart
        product.save()

        item.delete()
    
    Cart.objects.filter(username=username).delete()
    orders = Order.objects.filter(customer=user)
    return render(request, 'order.html', {'orders': orders})

def my_order(request):
    username=request.session.get('username')
    user=Customer.objects.get(username=username)
    orderd_products=Order.objects.filter(customer=user)
    return render(request,'order.html',{'orders':orderd_products})

from django.shortcuts import render, redirect
from .models import Category

def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('categoryName')
        if category_name:
            category = Category.objects.create(name=category_name)
            category.save()
            return redirect('admin')  
    return render(request, 'admin.html')

def admin_side(request):
    
    return render(request, 'admin.html')

def all_product(request):
    products = Product.objects.all()
    return render(request, 'all_product.html', {'products': products})

def all_seller(request):
    sellers = Owner.objects.all()
    return render(request, 'all_seller.html', {'sellers': sellers})

def all_customer(request):
    customers = Customer.objects.all()
    return render(request, 'all_customer.html', {'customers': customers})
    


    
