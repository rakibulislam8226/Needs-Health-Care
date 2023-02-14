from django.shortcuts import render, redirect
from . import forms
from . import models
from django.http import Http404
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
 

def create_ambulance(request):
    form = forms.AmbulanceForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Create successfully.')
        return redirect("/")
    return render(request,'ambulance/ambulance.html',{'form':form})


def ambulance_list(request):
    dataset = models.Ambulance.objects.all()
    context = {
        'dataset':dataset,
        
    }
    return render(request,'ambulance/ambulance_listview.html',context)


 
def ambulance_detail_view(request,_id):
    try:
        data = models.Ambulance.objects.get(id =_id)
        answers = models.Ambulance_hire.objects.filter(ambulance = data)
    except models.Ambulance.DoesNotExist:
        raise Http404('Data does not exist')
    
    # if request.method =="POST":
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     number = request.POST['number']
    #     location = request.POST['location']
    #     ambulance = request.POST['ambulance']
    #     obj = models.Ambulance_hire(name=name, number=number, email=email, location=location, ambulance=ambulance)
    #     #for email me start#
    #     # send_mail(
    #     #     f'You are hired from {answers.name}' ,
    #     #     f'Customer contract number: {answers.number} \n Pickup location- {answers.location}.\n Thank you. Stay connected with Needs Healthcare.',
    #     #     'settings.DEFAULT_FROM_EMAIL',
    #     #     [data.driver_email, 'faria.nova.27@gmail.com','sadiaprapti754@gmail.com', 'rakibkhan9065@gmail.com'],
    #     #     fail_silently=False,
    #     # )
    #     #for email me end#
    #     obj.save()
    #     messages.success(request, 'Ambulance hire submit successfully.')
    #     return redirect('/')
    
    # context = {

    # }
    # return render(request,'ambulance/ambulance_details.html',context)
     
    if request.method == 'POST':
        form = forms.Ambulance_hireForm(request.POST)
        if form.is_valid():
            answers = models.Ambulance_hire(name= request.user.username,
            number=form.cleaned_data['number'],
            email=form.cleaned_data['email'],
            location=form.cleaned_data['location'],
            ambulance=data)

            #for email me start#
            send_mail(
                f'You are hired from {answers.name}' ,
                f'Customer contract number: {answers.number} \n Pickup location- {answers.location}.\n Thank you. Stay connected with Needs Healthcare.',
                'settings.DEFAULT_FROM_EMAIL',
                [data.driver_email, 'faria.nova.27@gmail.com','sadiaprapti754@gmail.com', 'rakibkhan9065@gmail.com'],
                fail_silently=False,
            )
            #for email me end#
            answers.save()
            messages.success(request, 'Successfully request for ambulence.')
            return redirect(f'/ambulances')
    else:
        form = forms.Ambulance_hireForm()
 
    context = {
            'data':data,
            'form':form,
            'answers':answers,
        }
    return render(request,'ambulance/ambulance_details.html',context)