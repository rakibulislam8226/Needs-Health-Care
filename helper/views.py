from django.shortcuts import render, redirect
from . models import Get_touch,CreateQuery, Ambulance
from . forms import CreateQueryForm, AmbulanceForm
from django.contrib import messages
from django.core.mail import send_mail
from querys import models
from django.views import generic


# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #for email me start#
        data={
        'name':name,
        'email':email,
        'subject':subject,
        'message':message,
        }
        complain = ''' 
        Message are: {}
        from: {}
        '''.format(data['message'], data['email'])
        send_mail(data['email'],complain, '',['rakibkhan9065@gmail.com','sadiaprapti754@gmail.com'])
        #for email me end#

        obj = Get_touch(name=name, subject=subject, email=email, message=message)
        messages.success(request,'Feedback Submit Successfully.')
        obj.save()

    # latest post
    latest_posts = models.Post.objects.all()[:3]
             
    context={
        'latest_posts':latest_posts,
    }
    return render(request, 'base/index.html', context)


def appointment(request):
    if request.method=="POST":
        form = CreateQueryForm(request.POST)
        
        if form.is_valid():
            #for email me start#

            name = request.POST['name']
            email = request.POST['email']
            describe = request.POST['describe']
            data={
            'name':name,
            'email':email,
            'describe':describe,
            }
            complain = ''' 
            Name: {}
            from: {}
            Query are: {}
            '''.format(data['name'],data['email'], data['describe'])
            send_mail(data['email'],complain, '',['rakibkhan9065@gmail.com','sadiaprapti754@gmail.com'])
            #for email me end#  

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


# class AmbulanceList(generic.ListView):
#     queryset = Ambulance.objects.all()
#     template_name = 'ambulance/ambulance_listview.html'

def ambulance_list(request):
    ambulance = Ambulance.objects.all()
    if request.method == 'POST':
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            return redirect('/ambulance')
    else:
        form = AmbulanceForm()
        context = {
            'ambulance':ambulance,
            'form':form,
        }
    return render(request,'ambulance/ambulance_listview.html',context)


def create_ambulance(request):
    if request.method=="POST":
        form = AmbulanceForm(request.POST, request.FILES)
        if form.is_valid(): 
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request,'Query submit Successfully.')
            return redirect('/')
    else:
        form=AmbulanceForm()

    return render(request, 'ambulance/ambulance.html',{'form':form})


