from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'index.html')
def shop(request):
  return render(request,'shop.html')
def cart(request):
  return render(request,'cart.html')
def checkout(request):
  return render(request,'checkout.html')
def departments(request):
  return render(request,'departments.html')
def services(request):
  return render(request,'services.html')
def doctor(request):
  return render(request,'doctor.html')