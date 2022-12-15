from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from django.views.generic import CreateView
from .forms import PatientSignUpForm,DoctorSignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    doctors = models.Doctor.objects.all()
    patients = models.Patient.objects.all()
    context ={
        'doctors': doctors,
        'patients': patients,
    }
    return render(request,'home.html', context)


class PatientSignUpView(CreateView):
    model = models.User
    form_class = PatientSignUpForm
    template_name = 'userprofile/signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Patient'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
    
    
class DoctorSignUpView(CreateView):
    model = models.User
    form_class = DoctorSignUpForm
    template_name = 'userprofile/signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Doctor'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.info(self.request, "Thank you for your signup. Our admin will verify you ASAP. After approve you account will be active.")
        return redirect('login')


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="userprofile/login.html", context={"login_form":form})

def logout_view(request):
    logout(request)
    return redirect('/')
    # Redirect to a success page.



