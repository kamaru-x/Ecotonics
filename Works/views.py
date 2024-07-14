from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from Core.models import ServiceCategory,Service
from Works.models import ServiceCall
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

#----------------------------------- SERVICE CALLS -----------------------------------#

@login_required
def service_calls(request):
    calls = ServiceCall.objects.all()

    context = {
        'page' : 'service-calls',
        'calls' : calls
    }
    return render(request,'Backend/Work/service-calls.html',context)

#----------------------------------- ADD SERVICE CALL -----------------------------------#

@login_required
def add_service_call(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        description = request.POST.get('description')

        try:
            ServiceCall.objects.create(Name=name,Location=location,Number=mobile,Email=email,Description=description)
            messages.success(request,'Service call added successfully ... !')
            return redirect('service-calls')
        except:
            messages.warning(request,'Something went wrong ... !')
            return redirect('add-service-call')

    context = {
        'page' : 'service-calls',
    }
    return render(request,'Backend/Work/add-service-call.html',context)
