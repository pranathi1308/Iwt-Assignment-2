from django.shortcuts import render
from django.http import HttpResponse
from .forms import usersform
from .models import users
def home(request):
    return render(request,'homepage.html')
def register(request):
    context ={}
    form = usersform(request.POST or None, request.FILES or None)
    context['form']= form
    if form.is_valid():
        form.save()
        return render(request,'homepage.html')
    else:
        return render(request,'registration.html',context)
def allusers(request):
    b=users.objects.all()
    return render(request,'users.html',{'users':b})