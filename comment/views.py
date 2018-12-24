from django.shortcuts import render
from .models import Comment
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/rating/redirect/')
def comment(request):
	template = "comment_simple.html"

	if request.POST:
		content = request.POST["comment"]
		author = request.user.username
		comment =  Comment(content=content, author=author)

		comment.save()




	comments = Comment.objects.all().order_by('time')


	context = {
				"comments": comments[::-1],

				}


	return render(request, template, context)



