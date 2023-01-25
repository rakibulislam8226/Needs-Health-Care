from django.shortcuts import render
from appointment.models import Patients
from querys.models import Post ,AnswerPost
from django.http import Http404


# Create your views here.
def doctors_dashboard(request):
  all_appointments = Patients.objects.all()
  all_querys = Post.objects.all()
  answer_query = AnswerPost.objects.all()
  

  context = {
    'all_appointments':all_appointments,
    'all_querys':all_querys,
    'answer_query':answer_query
  }
  return render(request, 'doctors_dashboard/doctors_dashboard.html', context)


def query_view(request, _id):
  try:
    data = Post.objects.get(id =_id)
    answers_query = AnswerPost.objects.filter(post = data)
  except Post.DoesNotExist:
    raise Http404('Data does not exist.')
  
  context = {
  'answers_query':answers_query,

  }
  return render(request, 'doctors_dashboard/doctors_query_view.html', context)