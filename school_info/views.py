from django.shortcuts import render

# Create your views here.
def school_info(request):
	template = "school_info.html"

	context = {
				}


	return render(request, template, context)