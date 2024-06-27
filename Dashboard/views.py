from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Dashboard.models import Site,Transaction,Transaction_Category
from django.contrib import messages

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    context = {
        'page' : 'dashboard'
    }
    return render(request,'Backend/Dashboard/dashboard.html',context)

#----------------------------------- SITES -----------------------------------#

@login_required
def sites(request):
    sites = Site.objects.all().order_by('-id')
    context = {
        'page' : 'sites',
        'sites' : sites
    }
    return render(request,'Backend/Sites/sites.html',context)

#----------------------------------- CREATE SITE -----------------------------------#

@login_required
def create_site(request):
    sites = Site.objects.all()
    if request.method == 'POST':
        name = request.POST.get('siteName')
        location = request.POST.get('siteLocation')
        contact = request.POST.get('contactNumber')
        email = request.POST.get('emailAddress')

        try:
            Site.objects.create(Name=name,Location=location,Contact=contact,Mail=email)
            messages.success(request,'New Site Added Successfully ... !')
            return redirect('sites')
        except Exception as exception:
            messages.warning(request,'Something Went Wrong Please Try Again ... !')
            return redirect('create-site')


    context = {
        'page' : 'sites',
        'sites' : sites
    }
    return render(request,'Backend/Sites/site-create.html',context)

#----------------------------------- CATEGORIES -----------------------------------#

@login_required
def categories(request):
    categories = Transaction_Category.objects.all().order_by('-id')
    context = {
        'page' : 'cashflow',
        'categories' : categories,
        'sub_page' : 'categories',
    }
    return render(request,'Backend/Cashflow/categories.html',context)

#----------------------------------- ADD CATEGORY -----------------------------------#

@login_required
def add_category(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ctype = request.POST.get('type')

        try:
            Transaction_Category.objects.create(Title=title,Type=ctype)
            messages.success(request,'New transaction category added successfully .. !')
        except:
            messages.warning(request,'Something went wrong please try again ... !')

    return redirect('categories')

#----------------------------------- DELETE CATEGORY -----------------------------------#

@login_required
def delete_category(request,cid):
    category = Transaction_Category.objects.get(id=cid)
    category.delete()
    messages.warning(request,'Category deleted successfully ... !')
    return redirect('categories')

#----------------------------------- TRANSACTIONS -----------------------------------#

@login_required
def transactions(request):
    categories = Transaction_Category.objects.all().order_by('Type')
    transactions = Transaction.objects.all().order_by('-id')
    context = {
        'categories' : categories,
        'transactions' : transactions,
        'page' : 'cashflow',
        'sub_page' : 'transactions'
    }
    return render(request,'Backend/Cashflow/transactions.html',context)

#----------------------------------- ADD TRANSACTION -----------------------------------#

@login_required
def add_transaction(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        cid = request.POST.get('category')
        amount = request.POST.get('amount')

        category = Transaction_Category.objects.get(id=cid)

        try:
            Transaction.objects.create(Title=title,Category=category,Amount=amount)
            messages.success(request,'New transaction added successfully .. !')
        except:
            messages.warning(request,'Something went wrong please try again ... !')

    return redirect('transactions')

#----------------------------------- DELETE CATEGORY -----------------------------------#

@login_required
def delete_transaction(request,tid):
    transaction = Transaction.objects.get(id=tid)
    transaction.delete()
    messages.warning(request,'Transaction deleted successfully ... !')
    return redirect('transactions')