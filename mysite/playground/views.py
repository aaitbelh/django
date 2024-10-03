from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
from . import userauth

@csrf_exempt
def login_page(request):
    return render(request, 'hello.html')


@csrf_exempt
def say_hello_To(request):
	if request.user.is_authenticated :
		return HttpResponse(f"hello {request.user}")
	else:
		messages.info(request, "you are not logged yet")
		return redirect('/')

def home_page(request):
    return HttpResponse("homepage")

@csrf_exempt
def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/hello/')
		else:
			us = User.objects.create_user(username, "lennon@thebeatles.com", password)
			us.save()
			return redirect('/')
