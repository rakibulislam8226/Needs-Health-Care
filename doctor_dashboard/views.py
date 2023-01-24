from django.shortcuts import render
from appointment.models import Patients
from querys.models import Post


# Create your views here.
def doctors_dashboard(request):
  all_appointments = Patients.objects.all()
  all_querys = Post.objects.all()

  context = {
    'all_appointments':all_appointments,
    'all_querys':all_querys,

  }
  return render(request, 'doctors_dashboard/doctors.html', context)