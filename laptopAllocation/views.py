
import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render

from laptopAllocation.models import Allocation, Batch, Laptop, Student

allocation_notification = None

def INDEX(request):
    return redirect('laptop')

def LAPTOP(request):
    laptops = Laptop.objects.all()
    context = {
        'laptops':laptops
    }
    return render(request,"laptop.html",context)

def LAPTOP_CREATE(request):
    if request.method == "POST":
        laptop = Laptop(
            serial_number = request.POST.get('serial_number'),
            model_name = request.POST.get('model_name'),
        )
        laptop.save()
    return redirect('laptop')

def LAPTOP_UPDATE(request,id):
    if request.method == "POST":
        laptop = Laptop(
            id = id,
            serial_number = request.POST.get('serial_number'),
            model_name = request.POST.get('model_name'),
        )
        laptop.save()
    return redirect('laptop')

def LAPTOP_DELETE(request,id):
    laptop = Laptop.objects.filter(id=id)
    laptop.delete()
    return redirect('laptop')


def BATCH(request):
    batches = Batch.objects.all()
    context = {
        'batches':batches
    }
    return render(request,"batch.html",context)

def BATCH_CREATE(request):
    if request.method == "POST":
        batch = Batch(
            batch_number = request.POST.get('batch_number'),
            time_slot = request.POST.get('time_slot'),
        )
        batch.save()
    return redirect('batch')

def BATCH_UPDATE(request,id):
    if request.method == "POST":
        batch = Batch(
            id = id,
            batch_number = request.POST.get('batch_number'),
            time_slot = request.POST.get('time_slot'),
        )
        batch.save()
    return redirect('batch')

def BATCH_DELETE(request,id):
    batch = Batch.objects.filter(id=id)
    batch.delete()
    return redirect('batch')

def STUDENT(request):
    global allocation_notification
    students = Student.objects.all()
    batches = Batch.objects.all()
    def dateMapFunction(s):
        s.date_of_joining = s.date_of_joining.strftime('%Y-%m-%d')
        return s
    students = tuple(map(dateMapFunction,students))
    context = {
        'batches':batches,
        'students':students,
        'allocation':allocation_notification
    }

    # Clear notification
    allocation_notification = None
    return render(request,"student.html",context)

def STUDENT_CREATE(request):
    global allocation_notification
    if request.method == "POST":
        batch_number = request.POST.get('batch')
        batch = Batch.objects.get(batch_number=batch_number)
        student = Student(
            full_name = request.POST.get('full_name'),
            address = request.POST.get('address'),
            phone = request.POST.get('phone'),
            date_of_joining = request.POST.get('date_of_joining'),
            company_laptop_required = request.POST.get('company_laptop_required') == 'True',
            batch = batch,
        )
        student.save()

        if student.company_laptop_required:
            allocation_notification = allocateLaptop(student)

    return redirect('student')

def STUDENT_UPDATE(request,id):
    if request.method == "POST":
        batch_number = request.POST.get('batch')
        batch = Batch.objects.get(batch_number=batch_number)
        student = Student(
            id = id,
            full_name = request.POST.get('full_name'),
            address = request.POST.get('address'),
            phone = request.POST.get('phone'),
            date_of_joining = request.POST.get('date_of_joining'),
            company_laptop_required = request.POST.get('company_laptop_required') == 'True',
            batch = batch,
        )
        student.save()
    return redirect('student')

def STUDENT_DELETE(request,id):
    student = Student.objects.filter(id=id)
    student.delete()
    return redirect('student')

def ALLOCATION(request):
    allocations = Allocation.objects.all()
    context = {
        'allocations':allocations
    }
    return render(request,"allocation.html",context)

def allocateLaptop(student):
    batch = student.batch
    laptops = Laptop.objects.all()
    laptop = None

    # Iterate through all laptops till a laptop without allocation is found
    for l in laptops:
        # Get all allocations that were done for a laptop
        allocations = Allocation.objects.filter(laptop=l)

        # Filter above allocations that have the same batch as the student that needs the laptop
        allocations_to_batch = filter(lambda a: batch==a.student.batch, allocations)
        
        # If filtered out allocations are empty then this laptop can be allocated 
        if len(list(allocations_to_batch)) == 0:
            laptop = l
            break
    
    if laptop == None:
        return None

    allocation = Allocation(
        student = student,
        laptop = laptop,
        date_of_allocation = datetime.datetime.now(),
    )
    allocation.save()

    return allocation

