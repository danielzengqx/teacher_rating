# -*- coding: utf-8 -*-
# coding=gbk

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.conf import settings 
# from models import User
from django.contrib.auth.models import User
from django.core.mail import send_mail
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
def auth_mail(user):
	print "sending email"
	send_mail(
    '账号注册通知',
    '账号信息：\n姓名： %s\n学号： %s\n班级： %s\n用户名： %s\n' %(user.profile.firstname + user.profile.lastname, user.profile.school_num, user.profile.class_num, user.username),
    'cheer_zeng@163.com',
    ['cheer_zeng@163.com'],
    fail_silently=False,
)

# Create your views here.
def register(request):
	# registerInfo = {'username':'用户名', 'password':'密码','pwdconfirm':'确认密码', 'email':'邮箱'}
	context = {}
	template = "register.html"

	return render(request,template, context)


import uuid 
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = User.objects.get(ref_id=ref_id)
		return id_exists
	except:
		return ref_id



def signup(request):
	print request.POST
	user = User.objects.create_user(request.POST['username'].strip(), request.POST['email'].strip(), request.POST['password'].strip())
	user.profile.school_num = request.POST['school_num']
	user.profile.class_num = request.POST['class_num']
	user.first_name = request.POST["firstname"]
	user.last_name = request.POST["lastname"]

	# user.is_active = False
	user.save()	
	# auth_mail(usernameer)



	return HttpResponseRedirect('/')

def success(request):
	# questions_preview = [1,2,3,4,5]
	context = {}
	template = "register.html"

	return HttpResponse("Success")
