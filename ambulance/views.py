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
     
    if request.method == 'POST':
        form = forms.Ambulance_hireForm(request.POST)
        if form.is_valid():
            answers = models.Ambulance_hire(name= request.user.username,
            number=form.cleaned_data['number'],
            location=form.cleaned_data['location'],
            ambulance=data)

            #for email me start#
            send_mail(
                f'You are hired from {answers}' ,
                f'number {answers.number} and location {answers.location}',
                'cartoonbazar@gmail.com',
                [data.driver_email, 'rakibkhan9065@gmail.com'],
                fail_silently=False,
            )
            #for email me end#

            answers.save()
            messages.success(request, 'successfully request for ambulence.')
            return redirect(f'/ambulances')
    else:
        form = forms.Ambulance_hireForm()
 
    context = {
            'data':data,
            'form':form,
            'answers':answers,
        }
    return render(request,'ambulance/ambulance_details.html',context)