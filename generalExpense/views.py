from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vehicle,Vehicleexpense,Customer,Dailyexpense
from .forms import ExpensesForm,DailyexpensesForm

from .filters import VehicleexpenseFilter,DailyexpenseFilter

# Create your views here.

@login_required(login_url='login')
def dashboard(request):

    vehicles = Vehicle.objects.all()
    vehicleexpenses = Vehicleexpense.objects.all()[:5]
    customers =Customer.objects.all()

    context = {'customers':customers,'vehicleexpenses':vehicleexpenses,
               }
    return render(request,'generalExpense/dashboard.html',context)

@login_required(login_url='login')

def customer_stop(request,pk):

    customers = Customer.objects.get(id=pk)
    vehicleexpenses = customers.vehicleexpense_set.all()

    dailyexpenses = customers.dailyexpense_set.all()

    vehicleFilter = VehicleexpenseFilter(request.GET,queryset = vehicleexpenses )
    vehicleexpenses = vehicleFilter.qs

    dailyFilter = DailyexpenseFilter(request.GET, queryset = dailyexpenses)
    dailyexpenses = dailyFilter.qs

    #sum the total expenses for individual customer,reference from ChatGPT
    totalexpense = sum(Vehicleexpense.price for Vehicleexpense in vehicleexpenses)
    totaldailyexpense = sum(Dailyexpense.price for Dailyexpense in dailyexpenses)
    totalspend = totalexpense + totaldailyexpense 
    

    #<h5 style="text-align:center;padding:2px;"></h5>

    context = {'vehicleexpenses':vehicleexpenses,'customers':customers,
               'totalexpense':totalexpense,'dailyexpenses':dailyexpenses,
               'totaldailyexpense':totaldailyexpense,'totalspend':totalspend,
               'vehicleFilter':vehicleFilter,'dailyFilter':dailyFilter,
               }
    return render(request,'generalExpense/customer.html',context)

def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    vehicleexpenses = customers.vehicleexpense_set.all()
    dailyexpenses = customers.dailyexpense_set.all()

    filter_type = request.GET.get('filter_type')
    if filter_type == 'vehicle':
        vehicleFilter = VehicleexpenseFilter(request.GET, queryset=vehicleexpenses)
        vehicleexpenses = vehicleFilter.qs
        totalexpense = sum(Vehicleexpense.price for Vehicleexpense in vehicleexpenses)
        totaldailyexpense = 0  # Set the total daily expense to 0 as only the vehicle filter is selected
    elif filter_type == 'daily':
        dailyFilter = DailyexpenseFilter(request.GET, queryset=dailyexpenses)
        dailyexpenses = dailyFilter.qs
        totalexpense = 0  # Set the total expense to 0 as only the daily filter is selected
        totaldailyexpense = sum(Dailyexpense.price for Dailyexpense in dailyexpenses)
    else:
        # No filter selected, apply default behavior
        totalexpense = sum(Vehicleexpense.price for Vehicleexpense in vehicleexpenses)
        totaldailyexpense = sum(Dailyexpense.price for Dailyexpense in dailyexpenses)

    totalspend = totalexpense + totaldailyexpense

    context = {
        'vehicleexpenses': vehicleexpenses,
        'customers': customers,
        'totalexpense': totalexpense,
        'dailyexpenses': dailyexpenses,
        'totaldailyexpense': totaldailyexpense,
        'totalspend': totalspend,
        'vehicleFilter': vehicleFilter if filter_type == 'vehicle' else None,
        'dailyFilter': dailyFilter if filter_type == 'daily' else None,
    }
    return render(request, 'generalExpense/customer.html', context)



@login_required(login_url='login')
def addVehicleexpense(request,pk):
    customer = get_object_or_404(Customer, id=pk)
    

    if request.method == 'POST':

        form = ExpensesForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit = False)
            form_data.customer = customer
            customer_id = customer.id
           
            form_data.save()

            return redirect('customer', pk=customer_id)
    else:
        form = ExpensesForm()

    context = {'form':form}
    return render(request,'generalExpense/AddExpensesForm.html',context)

@login_required(login_url='login')
def updateVehicleexpense(request,pk):
    #customer = get_object_or_404(Customer, id=pk)
    vehicleexpenses = Vehicleexpense.objects.get(id=pk)
 
    form = ExpensesForm(instance = vehicleexpenses)

    if request.method == 'POST':

        form = ExpensesForm(request.POST,instance = vehicleexpenses)
        if form.is_valid():
            form.save()
            customer_id = vehicleexpenses.customer.id
            

            return redirect('customer', pk=customer_id)

    context = {'form':form}
    return render(request,'generalExpense/AddExpensesForm.html',context)

@login_required(login_url='login')
def deleteVehicleexpense(request,pk):
    vehicleexpenses = Vehicleexpense.objects.get(id=pk)
    customer_id = vehicleexpenses.customer.id

    if request.method == 'POST':
        vehicleexpenses.delete()
        return redirect('customer', pk=customer_id)
    
    context={}
    return render(request,'generalExpense/DeleteExpenses.html',context)

@login_required(login_url='login')
def addDailyexpense(request,pk):
    customer = get_object_or_404(Customer, id=pk)
    

    if request.method == 'POST':

        form = DailyexpensesForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit = False)
            form_data.customer = customer
            customer_id = customer.id
           
            form_data.save()

            return redirect('customer', pk=customer_id)
    else:
        form = DailyexpensesForm()

    context = {'form':form}
    return render(request,'generalExpense/AddDailyexpensesForm.html',context)


@login_required(login_url='login')
def updateDailyexpense(request,pk):
    #customer = get_object_or_404(Customer, id=pk)
    dailylexpense = Dailyexpense.objects.get(id=pk)
 
    form = DailyexpensesForm(instance = dailylexpense)

    if request.method == 'POST':

        form = DailyexpensesForm(request.POST,instance = dailylexpense)
        if form.is_valid():
            form.save()
            customer_id = dailylexpense.customer.id
            

            return redirect('customer', pk=customer_id)

    context = {'form':form}
    return render(request,'generalExpense/AddDailyexpensesForm.html',context)

@login_required(login_url='login')
def deleteDailyexpense(request,pk):
    dailyexpense = Dailyexpense.objects.get(id=pk)
    customer_id = dailyexpense.customer.id

    if request.method == 'POST':
        dailyexpense.delete()
        return redirect('customer', pk=customer_id)
    
    context={}
    return render(request,'generalExpense/DeleteDailyexpenses.html',context)


