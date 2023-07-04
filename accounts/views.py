from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomerForm,CreateCustomerForm
from generalExpense.models import Customer
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User

# Create your views here.

def signup(request):

    form = CreateCustomerForm()

    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        
        if form.is_valid():
            user = form.save()
            
            print('username :',username)

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            user = Customer.objects.create(user=user,name=username,email=email)

            messages.success(request,"account was created for "+ username)
            return redirect('login')
        
    context={'form':form}
    return render(request,'accounts/signup.html',context)

def loginPage(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'Username or password incorrect')

    context = {}
    return render(request,'accounts/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def accountSettings(request):
    customer = get_object_or_404(Customer, user=request.user)
    
    print('customer:',customer)
    print('customer:',customer.name)
    print('customer:',customer.email)

    form = CustomerForm(instance = customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    
    context={'form':form}
    return render(request,'accounts/account_Settings.html',context)
