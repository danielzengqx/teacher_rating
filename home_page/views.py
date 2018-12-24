from django.shortcuts import render
from django.conf import settings 

# Create your views here.
def home(request):
	context = {
			"user": request.user.username
	}
	template = "new.html"


	return render(request,template, context)

