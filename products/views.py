from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .filters import *
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *



def user(request):
    orders=Order.objects.all()
    products=Product.objects.all()

    userorders= request.user
    return render(request, 'products/user.html')



def register(request):
    form = RegistrationForm()
    if request.method =="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print("Saqlandi")
            form.save()

            return redirect('/login/')
        else:
            print(form.errors)
    return render(request,'products/register.html',{"form":form})




def user_login(request):
    form = RegistrationForm()
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')

    # context = {"form": form}

    return render(request, 'products/login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login/")

@login_required(login_url='/login/')    
@allowed_users(allowed_role=["admin"])
def home(request):
    categories=Category.objects.all()
    products =Product.objects.all()

    pfilter= ProductFilter(request.GET, queryset=products)
    products=pfilter.qs


    data= {'products':products,'pfilter':pfilter}

    return render(request, "products/home.html",data)


@allowed_users(allowed_role=["admin"])
def products(request):
    my_dict = {"products": Product.objects.all(),}

    return render(request, "products/products.html",
                  context=my_dict)


@allowed_users(allowed_role=["admin"])
def category(request):
    my_dict = {"categorys": Category.objects.all(),}

    return render(request, "products/category.html",
                  context=my_dict)


@allowed_users(allowed_role=["admin"])
def customer(request):
    my_dict = {"customers": Customer.objects.all(),}

    return render(request, "products/customer.html",
                  context=my_dict)


@allowed_users(allowed_role=["admin"])
def status(request):
    my_dict = {"status": Status.objects.all(),}

    return render(request, "products/status.html",
                  context=my_dict)


@allowed_users(allowed_role=["admin"])
def order(request):
    my_dict = {"orders": Order.objects.all(),}

    return render(request, "products/order.html",
                  context=my_dict)




def createProduct(request):
    if request.method == "POST":
        productFrom = ProductForm(data=request.POST)
        print(request.POST)
        if productFrom.is_valid():
            productFrom.save(commit=True)
            return redirect("/product/")
    else:
        productFrom = ProductForm()

    return render(request, "products/create/createProduct.html", context={
            "form": productFrom,
        })
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        productForm = ProductForm(data=request.POST, instance=product)
        if productForm.is_valid():
            productForm.save()
            return redirect("/product/")
    else:
        productForm = ProductForm(instance=product)

    return render(request, "products/update/updateProduct.html", context={
            "form": productForm,
        })
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/product/')
    return render(request, 'products/delete/deleteProduct.html', context={'item':product})
def createCategory(request):
    if request.method == "POST":
        categoryForm = CategoryForm(data=request.POST)
        print(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect("/category/")
    else:
        categoryForm = CategoryForm()

    return render(request, "products/create/createCategory.html", context={
            "form": categoryForm,
        })
def updateCategory(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == "POST":
        categoryForm = CategoryForm(data=request.POST, instance=category)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect("/category/")
    else:
        categoryForm = CategoryForm(instance=category)

    return render(request, "products/update/updateCategory.html", context={
            "form": categoryForm,
        })
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('/category/')
    return render(request, 'products/delete/deleteCategory.html', context={'item':category})
def createCustomer(request):
    if request.method == "POST":
        customerForm = CustomerForm(data=request.POST)
        print(request.POST)
        if customerForm.is_valid():
            customerForm.save(commit=True)
            return redirect("/customer/")
    else:
        customerForm = CustomerForm()

    return render(request, "products/create/createCustomer.html", context={
            "form": customerForm,
        })
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customerForm = CustomerForm(data=request.POST, instance=customer)
        if customerForm.is_valid():
            customerForm.save()
            return redirect("/customer/")
    else:
        customerForm = CustomerForm(instance=customer)

    return render(request, "products/update/updateCustomer.html", context={
            "form": customerForm,
        })
def deleteCustomer(request, pk):

    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/customer/')
    return render(request, 'products/delete/deleteCustomer.html', context={'item':customer})
def createStatus(request):
    if request.method == "POST":
        statusForm = StatusForm(data=request.POST)
        print(request.POST)
        if statusForm.is_valid():
            statusForm.save(commit=True)
            return redirect("/status/")
    else:
        statusForm = StatusForm()

    return render(request, "products/create/createStatus.html", context={
            "form": statusForm,
        })
def updateStatus(request, pk):
    status = Status.objects.get(id=pk)
    if request.method == "POST":
        statusForm = StatusForm(data=request.POST, instance=status)
        if statusForm.is_valid():
            statusForm.save()
            return redirect("/status/")
    else:
        statusForm = StatusForm(instance=status)

    return render(request, "products/update/updateStatus.html", context={
            "form": statusForm,
        })
def deleteStatus(request, pk):
    status = Status.objects.get(id=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('/status/')
    return render(request, 'products/delete/deleteStatus.html', context={'item':status})
def createOrder(request):
    if request.method == "POST":
        orderForm = OrderForm(data=request.POST)
        print(request.POST)
        if orderForm.is_valid:
            orderForm.save()
            return redirect("/order/")
    else:
        orderForm = OrderForm()

    return render(request, "products/create/createOrder.html", context={
            "form": orderForm})
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        orderForm = OrderForm(data=request.POST, instance=order)
        if orderForm.is_valid():
            orderForm.save()
            return redirect("/order/")
    else:
        orderForm = OrderForm(instance=order)

    return render(request, "products/update/updateOrder.html", context={
            "form": orderForm,
        })
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/order/')

    return render(request, 'products/delete/deleteOrder.html', context={'item':order})

