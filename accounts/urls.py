from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .views import ActivateAccount


urlpatterns = [
    # path('login/', views.loginuser, name='login'),
    # path('logout/', views.logoutuser, name='logout'),
    # path('register/', views.register, name='register'),
    # path('userprofile/', views.userprofile, name='userprofile'),
    # path('otherprofile/<int:id>/', views.otherprofile, name='otherprofile'),
    # path('userprofilecreate/', views.userprofilecreate, name='userprofilecreate'),
    # path('change_password/', views.change_password, name='change_password'),
    path('register/', views.index,name='register'),
    path('', views.home,name='index'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_view, name="logout_view"),
    path('patient-signup/', views.PatientSignUpView.as_view(), name='patient_signup'),
    path('doctor-signup/', views.DoctorSignUpView.as_view(), name='doctor_signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),



    path('reset/password/', PasswordResetView.as_view(template_name='userprofile/pass_reset.html'), name='password_reset'),

    path('reset/password/done/', PasswordResetDoneView.as_view(
    template_name='userprofile/pass_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    template_name='userprofile/pass_reset_confirm.html'), name='password_reset_confirm'),

    path('reset/done/', PasswordResetView.as_view(
    template_name='userprofile/pass_reset_complete.html'), name='password_reset_complete'),

]