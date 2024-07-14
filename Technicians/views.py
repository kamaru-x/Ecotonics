from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from U_Auth.models import User
from django.contrib import messages

# Create your views here.

#----------------------------------- TECHNICIANS -----------------------------------#

@login_required
def technicians(request):
    technicians = User.objects.all()

    context = {
        'page' : 'technicians',
        'sub_page' : 'technicians',
        'technicians' : technicians
    }
    return render(request,'Backend/Technicians/technicians.html',context)

#----------------------------------- ADD TECHNICIAN -----------------------------------#

@login_required
def add_technician(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.create(first_name=name,Place=location,Mobile=mobile,email=email,username=username)
            user.set_password(password)
            user.save()
            messages.success(request,'Technician added successfully ... !')
            return redirect('technicians')
        except Exception as exception:
            messages.warning(request,'Something Went wrong ... !')
            return redirect('add-technician')

    context = {
        'page' : 'technicians',
        'sub_page' : 'technicians',
    }
    return render(request,'Backend/Technicians/technician-add.html',context)

#----------------------------------- DELETE TECHNICIAN -----------------------------------#

@login_required
def delete_technician(request,technician_id):
    technician = User.objects.get(id=technician_id)
    technician.delete()
    messages.warning(request,'Technician deleted successfully ... !')
    return redirect('technicians')