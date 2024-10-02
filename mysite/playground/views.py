from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
# Create your views here.
from . import userauth

@csrf_exempt
def login_page(request):
    return render(request, 'hello.html')


@csrf_exempt
def say_hello_To(request):
    print("Hii")
    userauth.authenticateUser()
    return HttpResponse("hello")

def home_page(request):
    return HttpResponse("homepage")

@csrf_exempt
def login_user(request):
	if request.method == 'POST':
		print(request)	
		# username = request.POST['USER']
		# password = request.POST['password']
		# user = authenticate(username="john", password="secret")
		# if user is not None:
		# 	login(request, user)
		# 	return redirect('hello/')
		# else:
		# 	return render(request, 'hello.html')
