from django.shortcuts import render, redirect
from . models import Get_touch,CreateQuery
from . forms import CreateQueryForm
from django.contrib import messages


# Create your views here.
def home(request):
    # if request.method == "POST":
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     subject = request.POST['subject']
    #     message = request.POST['message']

    #     obj = Get_touch(name=name, subject=subject, email=email, message=message)
    #     obj.save()

    # if request.method == "POST":
    #     qname = request.POST['qname']
    #     qemail = request.POST['qemail']
    #     qphone = request.POST['qphone']
    #     qdate = request.POST['qdate']
    #     qdepartment = request.POST['qdepartment']
    #     qdescribe = request.POST['qdescribe']

    #     obj = CreateQuery(qname=qname, qemail=qemail, qphone=qphone, qdate=qdate,qdepartment=qdepartment,qdescribe=qdescribe)
    #     obj.save()
             
    # context={
    # }
    return render(request, 'base/index.html')


def appointment(request):
    if request.method=="POST":
        form = CreateQueryForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request,'Query created Successfully.')
            return redirect('/')
    else:
        form=CreateQueryForm()

    return render(request, 'query.html',{'form':form})


def shop(request):
    return render(request, 'shop.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def departments(request):
    return render(request, 'departments.html')


def services(request):
    return render(request, 'services.html')


def doctor(request):
    return render(request, 'doctor.html')


def ambulance(request):
    return render(request, 'ambulance.html')
