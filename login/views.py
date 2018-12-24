from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.
def myLogin(request):
	template = "login.html"
	context = {}
	return render(request, template, context)



def auth(request):
	print "here is auth\n"
	if request.POST:
		print "in post"
		print request.POST
	username = request.POST['user_name'].strip()
	password = request.POST['password'].strip()
	user = authenticate(username=username, password=password)
	if user is not None:
		# return HttpResponse("Welcome")
		login(request, user)
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/register")


