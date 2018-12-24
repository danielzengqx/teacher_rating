from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.conf import settings
import os
# Create your views here.
def video(request):
	# user = request.user.username
	# email = request.user.email
	# user = "test"
	# email = "test@test.com"

	for f in settings.STATICFILES_DIRS:
		print "f: %s" %f


	video_all = dict()
	video_files = os.listdir(settings.STATICFILES_DIRS[0]+"/video/")
	for v in video_files:
		video_all[v.split('.')[0]] = v

	for i in video_files:
		print i

	template = "video.html"
	context = {
				"video_all": video_all
				}


	return render(request, template, context)
	# return HttpResponseRedirect("http://localhost:8000/")



