from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

# Create your views here.
def myLogout(request):
	logout(request)
    # Redirect to a success page.
	return HttpResponseRedirect("/")

