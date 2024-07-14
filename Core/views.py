from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Core.models import ServiceCategory,Service
from django.contrib import messages

# Create your views here.

#----------------------------------- SERVICES -----------------------------------#

@login_required
def services(request):
    categories = ServiceCategory.objects.all()
    services = Service.objects.all().order_by('Category')

    context = {
        'page' : 'services',
        'categories' : categories,
        'services' : services
    }
    return render(request,'Backend/Services/services.html',context)

#----------------------------------- ADD SERVICE -----------------------------------#

@login_required
def add_service(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        category = ServiceCategory.objects.get(id=category_id)
        title = request.POST.get('title')

        try:
            Service.objects.create(Category=category,Title=title)   
            messages.success(request,'New service added successfully ... !')
        except:
            messages.warning(request,'Something went wrong ... !')     
    return redirect('services')

#----------------------------------- DELETE SERVICE -----------------------------------#

@login_required
def delete_service(request,service_id):
    service = Service.objects.get(id=service_id)
    service.delete()
    messages.warning(request,'Service deleted successfully ... !')
    return redirect('services')