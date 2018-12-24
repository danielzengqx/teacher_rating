# -*- coding: utf-8 -*-
# coding=gbk

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rating.models import User, Profile, Teacher2, Student, Class, CourseForClass
# Create your views here.
import inspect
from django.contrib.auth.decorators import login_required

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno
def register(request):
	context = {}
	template = "teacher_signup.html"

	return render(request,template, context)




def signup(request):
	print request.POST
	user = User.objects.create_user(request.POST['username'].strip(), request.POST['email'].strip(), request.POST['password'].strip())
	user.profile.work_id = request.POST['work_id']
	user.profile.gender = request.POST['gender']
	user.first_name = request.POST['username'].strip()
	user.last_name = request.POST['lastname'].strip()
	# user.is_active = False
	user.save()	
	# auth_mail(user)



	return HttpResponseRedirect('/')


def success(request):
	# questions_preview = [1,2,3,4,5]
	context = {}
	template = "register.html"

	return HttpResponse("Success")	

@login_required(login_url='/rating/redirect/')
def setting(request):
	template = "setting.html"


	# wid = request.user.wid
	profile = Profile.objects.get(user=request.user)


	work_id = profile.work_id
	school_num = profile.school_num

	# return HttpResponseRedirect('/')
	if work_id:
		return HttpResponseRedirect("my_page/%s" %work_id)	
	elif school_num:
		return HttpResponseRedirect("stu_page/%s" %school_num)			
	else:
		# print lineno(), "Failed Reason, ", e
		return HttpResponse("不存在该资源, 请返回")

def my_page(request, work_id):
	template = "my_page.html"
	# work_id = '20170002'

	profile = Profile.objects.get(work_id=work_id)
	try:
		teacher =  Teacher2.objects.get(work_id=work_id)

	except Exception as e:
		print lineno(), "Failed Reason, ", e
		return HttpResponse("没有与您工号对应的教师信息， 请与管理员联系， 确保已加入数据库或工号录入正确。")



	score_total_percent = format(teacher.score_total/100,'.0%')
	context = {	
				"teacher": teacher,
				"name": teacher.name,
				"phone": teacher.phone,
				"email": profile.user.email,
				"major": teacher.major,
				'count': teacher.rater_count,
				"intro": teacher.intro,
				"score_total": int(round(teacher.score_total, 1)),
				"score_total_percent": score_total_percent,
				"courses": teacher.all_courses.all()

				}


	return render(request,template, context)

def edit_page(request, work_id):
	if request.POST:
		print request.POST
		

	template = "edit_page.html"
	# work_id = '20170002'

	print "here is edit_page"
	profile = Profile.objects.get(work_id=work_id)
	try:
		teacher =  Teacher2.objects.get(work_id=work_id)

	except Exception as e:
		print lineno(), "Failed Reason, ", e
		HttpResponse("不存在该资源")



	score_total_percent = format(teacher.score_total/100,'.0%')
	context = {	
				"teacher": teacher,
				"email": profile.user.email
				}


	return render(request,template, context)

def change_profile(request, work_id):
	if request.POST:
		print request.POST
		

		# template = "edit_page.html"
		# work_id = '20170002'
		# return 

		print "here is edit_page"
		# teacher = Teacher2.objects.get(work_id=work_id)
		try:
			teacher =  Teacher2.objects.get(work_id=work_id)
			# teacher.name = request.POST["name"]
			teacher.phone = request.POST["phone"]
			teacher.intro = request.POST["intro"]

			teacher.save()

			profile = Profile.objects.get(work_id=work_id)
			user = profile.user
			user.email = request.POST["email"]
			# set_password(request.POST["password"])
			user.save()




		except Exception as e:
			print lineno(), "Failed Reason, ", e
			HttpResponse("不存在该资源")


		return HttpResponseRedirect("/teacher_account/setting")

		# return render(request,template, context)


## For Student Account ###
def stu_page(request, school_num):
	template = "stu_page.html"
	# work_id = '20170002'


	profile = Profile.objects.get(user=request.user)
	class_name = Class.objects.get(name=profile.class_num)

	try:
		student = Student.objects.get(profile=request.user)
		student.save()

	except Exception as e:
		print lineno(), "Reason: ", e
		print "No Student,create one "
		student = Student(profile=request.user, class_name = class_name)


	courses = CourseForClass.objects.filter(class_name=class_name)

	course_t = dict()


	for course in courses:
		for teacher in Teacher2.objects.all():
			if course in teacher.all_courses.all():
				course_t[teacher] = course

	for k, v in course_t.items():
		print k, v


	print courses
	context = {	
				"student": student,
				# "courses": courses,
				"name": student.profile.username,
				"courses_teachers":  course_t
				}


	return render(request,template, context)



def redirect(request):
	print "here is redirect"
	template = "redirect_nosignin.html"

	context = {
				}







