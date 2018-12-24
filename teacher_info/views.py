# -*- coding: utf-8 -*-
# coding=gbk
from __future__ import division
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rating.models import Teacher2, RatingForTeacher, Profile, Major
# Create your views here.
from django.contrib.auth.decorators import login_required
import inspect
import os, subprocess
def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

def load_more(request, tab=1, page=0):
	print os.getcwd()
	os.system("cp /home/daniel/teacher/teacher_info_system/teacher_info/templates/page_tab1.html /home/daniel/teacher/teacher_info_system/rating/templates/page_tab%s.html" %tab)
	template = "page_tab%s.html" %tab
	page = int(page)

	teacher_major = dict()
	major = Major.objects.get(id=tab)
	print lineno(), major
	print lineno(), page

	teacher_major[major] = list()
	teachers = list()
	count = 0		
	for teacher in Teacher2.objects.filter(major=major)[:(page+1)*10]:
		if teacher.major.name == major.name:
			teachers.append(teacher)
			count += 1

	print teachers
	context = {
				"teachers": teachers,
				"teacher_major": teacher_major			
				}


	return render(request, template, context)
	# return HttpResponseRedirect("http://localhost:8000/")


def teacher_init():
	teachers =  Teacher2.objects.all()
	for t in teachers:
		# print "count %s type %s, star" %(t.score1_count, type(t.score1_count))
		if t.score_total == 0:
			# print "equals zero"
			t.stars_filled = ''
			t.stars_empty = 'xxxxx'
			t.save()
			# print "stars after %s" %t.stars_filled

def teacher_info(request, page=0):
	teacher_init()
	teachers =  Teacher2.objects.all()
	teachers_major1 = list()
	teachers_major2 = list()
	teachers_major3 = list()
	for t in teachers:
		if t.major == u"计算机":
			# print "here is teacher %s, name %s, major %s" %(t.tid, t.name, t.major)
			teachers_major1.append(t)
		elif t.major == u"音乐系":
			# print "here is teacher %s, name %s, major %s" %(t.tid, t.name, t.major)
			teachers_major2.append(t)
		else:
			teachers_major3.append(t)

	# template = "teacher_info.html"
	# template = "teacher_widget.html"
	# template = "profile.html"
	# template = "user_profile.html"
	template = "tab.html"

	teacher_major = dict()
	for major in Major.objects.all():
		teacher_major[major] = list()
		count = 0		
		for teacher in Teacher2.objects.all():
			if teacher.major.name == major.name and count < 10:
				teacher_major[major].append(teacher)
				count += 1



	print teacher_major
	page = int(page)


	context = {
				"teachers_major1": teachers_major1[page*10:(page+1)*10],
				"teachers_major2": teachers_major2[page*10:(page+1)*10],
				"teachers_major3": teachers_major3[page*10:(page+1)*10],
				"majors": Major.objects.all(),
				"teachers": Teacher2.objects.all()[page*10:(page+1)*10],
				"teacher_major": teacher_major

				}


	return render(request, template, context)
	# return HttpResponseRedirect("http://localhost:8000/")


import uuid 
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = User.objects.get(ref_id=ref_id)
		return id_exists
	except:
		return ref_id

def teacher_detail(request, id):
	try:
		teacher =  Teacher2.objects.get(id=id)
	except Exception as e:
		print lineno(), "Failed Reason, ", e
		HttpResponse("不存在该资源")

	template = "profile.html"

	try:
		profile = Profile.objects.get(work_id=teacher.work_id)
		email = profile.user.email
	except Exception as e:
		print lineno(), "Get Teacher Profile failed, Reason: ", e
		email = "教师未完善该信息"

	# print "email ", profile.user.email
	score_total_percent = format(teacher.score_total/100,'.0%')

	ranking = 1
	for t in Teacher2.objects.all():
		if t.score_total > teacher.score_total:
			ranking += 1

	context = {	
				"teacher": teacher,
				"name": teacher.name,
				"major": teacher.major,
				"email": email,
				'count': teacher.rater_count,
				"intro": teacher.intro,
				"score_total": int(round(teacher.score_total, 1)),
				"score_total_percent": score_total_percent,
				"ranking": ranking,
				"courses": teacher.all_courses.all()


				}


	return render(request, template, context)
