from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .forms import PatientForm, PatientAppointmentAnswerForm
from .models import Patients, Doctor, PatientAppointmentAnswer
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.
# @api_view(['POST',])

def create_view(request):
  default_user = {
    'user':request.user
  }

  form = PatientForm(initial=default_user)
  if request.method == 'POST':
    form = PatientForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Create successfully.')
      return redirect('/')
  return render(request, 'appointment/home.html', {'form': form})


# AJAX
def load_doctors(request):
  department_id = request.GET.get('department_id')
  doctors = Doctor.objects.filter(department_id=department_id).all()
  return render(request, 'appointment/doctor_dropdown_list_options.html', {'doctors': doctors})


def total_appointments(request):
  total = Patients.objects.all()


  context ={
    'total': total
  }
  return render(request ,'appointment/appointment_list.html', context)

 
def user_appointments(request,_id):
  try:
    data = Patients.objects.get(id =_id)
    answers = PatientAppointmentAnswer.objects.filter(patient = data)
  except Patients.DoesNotExist:
    raise Http404('Data does not exist')
    
  if request.method == 'POST':
    form = PatientAppointmentAnswerForm(request.POST)
    if form.is_valid():
      answers = PatientAppointmentAnswer(
      test=form.cleaned_data['test'],
      medicine_one=form.cleaned_data['medicine_one'],
      medicine_two=form.cleaned_data['medicine_two'],
      medicine_three=form.cleaned_data['medicine_three'],
      medicine_others=form.cleaned_data['medicine_others'],
      advice=form.cleaned_data['advice'],
      patient=data)
      answers.save()
      messages.success(request, 'successfully request for appointment.')
      return redirect(f'/')
  else:
      form = PatientAppointmentAnswerForm()

  context = {
    'data':data,
    'form':form,
    'record':answers,
  }
  return render(request,'appointment/appointment_details.html',context)



def render_to_pdf(template_src, context_dict={}):
  template = get_template(template_src)
  html = template.render(context_dict)
  response = HttpResponse(content_type='application/pdf')
  pdf_status = pisa.CreatePDF(html, dest=response)

  if pdf_status.err:
    return HttpResponse('Some errors were encountered <pre>' + html + '</pre>')

  return response


def prescription_pdf(request, _id):
  template_name = "appointment/prescription_pdf.html"
  records = PatientAppointmentAnswer.objects.get(id = _id)

  return render_to_pdf(
    template_name,
    {
      "record": records,
    },
  )