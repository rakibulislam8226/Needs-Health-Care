from django.shortcuts import render, redirect
from . models import Get_touch,CreateQuery
from . forms import CreateQueryForm
from django.contrib import messages
from django.core.mail import send_mail
from querys import models
from django.views import generic
from django.contrib.auth.decorators import login_required


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
        send_mail(data['email'],complain, '',['faria.nova.27@gmail.com','sadiaprapti754@gmail.com', 'rakibkhan9065@gmail.com'])
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


# @login_required
# def appointment(request):
    # if request.method=="POST":
    #     form = CreateQueryForm(request.POST)
        
    #     if form.is_valid():
    #         #for email me start#

    #         name = request.POST['name']
    #         email = request.POST['email']
    #         describe = request.POST['describe']
    #         data={
    #         'name':name,
    #         'email':email,
    #         'describe':describe,
    #         }
    #         complain = ''' 
    #         Name: {}
    #         from: {}
    #         Query are: {}
    #         '''.format(data['name'],data['email'], data['describe'])
    #         send_mail(data['email'],complain, '',['rakibkhan9065@gmail.com','sadiaprapti754@gmail.com','faria.nova.27@gmail.com'])
    #         #for email me end#  

    #         obj=form.save(commit=False)
    #         obj.user=request.user
    #         obj.save()
    #         messages.success(request,'Query created Successfully.')
    #         return redirect('/')
    # else:
    #     form=CreateQueryForm()

    # return render(request, 'others/appointment.html',{'form':form})


# class AmbulanceList(generic.ListView):
#     queryset = Ambulance.objects.all()
#     template_name = 'ambulance/ambulance_listview.html'


def emergency(request):
    return render(request, 'emergency/demo.html')