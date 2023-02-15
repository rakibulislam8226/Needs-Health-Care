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

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.contrib.auth.models import User
# from django.utils.encoding import force_text
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .tokens import AccountActivationTokenGenerator
from .tokens import account_activation_token
from django.views.generic import View, UpdateView
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('/')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('/')

def index(request):
    return render(request,'index.html')

def home(request):
    doctors = models.DoctorSignUp.objects.all()
    patients = models.PatientSignUp.objects.all()
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
    
    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     messages.info(self.request, "Your account created successfully. Thank you for your signup NeedsHealth Care.")
    #     return redirect('/')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True # Deactivate account till it is confirmed
            user.save()

            # mail activation work start #
            current_site = get_current_site(request)
            subject = 'Activate Your Needs Healthcare Account'
            message = render_to_string('userprofile/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            # end mail activation work #

            messages.success(request, ('Please Confirm your email to complete registration.'))
            return redirect('/')
        return render(request, self.template_name, {'form': form})
    
    
class DoctorSignUpView(CreateView):
    model = models.User
    form_class = DoctorSignUpForm
    template_name = 'userprofile/signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Doctor'
        return super().get_context_data(**kwargs)
    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     messages.info(self.request, "Thank you for your signup. Your account are active but our admin will verify you ASAP. After approve your profile will be update. Till you are a simple user.")
    #     return redirect('/')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False # Deactivate account till it is confirmed
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Needs Healthcare Account'
            message = render_to_string('userprofile/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            messages.success(request, ('Please Confirm your email to complete registration.'))
            return redirect('/')
        return render(request, self.template_name, {'form': form})


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



