from django.shortcuts import render
from appointment.models import Patients, PatientAppointmentAnswer
from querys.models import Post, AnswerPost
from django.http import Http404
from django.contrib import messages


# Create your views here.
def doctors_dashboard(request):
  all_appointments = Patients.objects.all()
  answer_appoinemtn = PatientAppointmentAnswer.objects.all()
  
  all_querys = Post.objects.all()
  answer_query = AnswerPost.objects.all()


  # pop up message start #
  querys = len(all_querys)
  ans_querys = len(answer_query)
  appointment = len(all_appointments)
  ans_appointment = len(answer_appoinemtn)

  if appointment > ans_appointment:
    messages.success(request, 'You have pending appointment for answer.')

  if querys > ans_querys:
    messages.success(request, 'You have pending query for answer.')
  # end pop up message #

  context = {
    'all_appointments':all_appointments,
    'all_querys':all_querys,
    'answer_query':answer_query,
  }
  return render(request, 'doctors_dashboard/doctors_dashboard.html', context)


def unanswer_query_view(request):
  totla_query = AnswerPost.objects.filter(name = True)
  # unanswer_query = AnswerPost.objects.filter(post__post = False)
  print(f'total {len(totla_query)}')
  # print(len(unanswer_query))

  context = {
    'totla_query':totla_query,
    # 'unanswer_query':unanswer_query
  }
  return render(request, 'doctors_dashboard/unanswer_query.html', context)

