from django.shortcuts import render, redirect
from . models import Get_touch,CreateQuery, AboutUs
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

        # send_mail(
        #     'Contract from',
        #     message,
        #     'settings.EMAIL_HOST_USER',
        #     [email,'rakibkhan9065@gmail.com'],
        #     fail_silently=False
        # )

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
        send_mail(data['email'],complain, '',['faria.nova.27@gmail.com','sadiaprapti754@gmail.com', 'rakibkhan9065@gmail.com'], fail_silently=False)
        #for email me end#

        obj = Get_touch(name=name, subject=subject, email=email, message=message)
        messages.success(request,'Feedback Submit Successfully.')
        obj.save()

    # latest post
    latest_posts = models.Post.objects.all()[:4]
    about_us = AboutUs.objects.all()
             
    context={
        'latest_posts':latest_posts,
        'about_us':about_us,
    }
    return render(request, 'base/index.html', context)




