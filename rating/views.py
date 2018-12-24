# -*- coding: utf-8 -*-
# coding=gbk
from __future__ import division 
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from models import Teacher2, Profile, RatingItem, ItemScore, RatingForTeacher
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
import json
import re
@login_required(login_url='/rating/redirect/')
def rating(request, id=0):
	user = request.user.username
	email = request.user.email
	# user = "test"
	# email = "test@test.com"

	if 	request.POST:
		print "here is rating post %s" %request.POST

		tid = request.POST['m1']
		try:
			teacher = Teacher2.objects.get(id=tid)
		except Exception as e:
			print "Get Teacher Faile."
			return HttpResponse("该老师不存在, 请返回检查是否已选择评分老师")


		try:
			rating_for_teacher = RatingForTeacher.objects.get(teacher = teacher)

		except Exception as e:
			print "Get rating for teacher failed, init one"
			rating_for_teacher = RatingForTeacher(teacher = teacher)
			rating_for_teacher.save()

		print "teacher id: %s" %tid
		for k, v in request.POST.items():
			result = re.search(r'rating_(\d+)', k)
			if result:
				score = int(v)
				print k, v, score

				item_id =result.group(1)
				print "rating_id: %s" %item_id

				print "teacher name: %s" %teacher.name

				rating_item = RatingItem.objects.get(id=item_id)
				try:
					item_score = ItemScore(item = rating_item, score=score, rater=user)
					item_score.save()
					print "ItemScore saved, item: %s, score: %s, rater: %s" %(rating_item, score, user)
				except Exception as e:
					print "Init ItemScore failed, Reason, ", e
					print "try to change an existed one"




				try:
					rating_for_teacher.item_score.add(item_score)
					rating_for_teacher.save()
				except Exception as e:
					print "Add for item failed, create one"
					rating_for_teacher.item_score.create(item_score)
					rating_for_teacher.save()


		teacher.add_rater(user)
		score_total  = 0
		for item_score in rating_for_teacher.item_score.all():
			score = item_score.score
			print "score: %s" %score

			score_total  += score
			print "total score %s" %score_total


		print "rater_count", teacher.rater_count
		print "before %s, this time %s" %(teacher.score_total, score_total)
		teacher.score_total = score_total /  teacher.rater_count

		stars = int(round(teacher.score_total/ 100 * 5 ))
		teacher.stars_filled = stars * 'x'
		teacher.stars_empty = (5 - stars) * 'x'
		teacher.save()
		print "stars", stars

		return HttpResponseRedirect("/teacher_info/detail/%s" %tid)
		# return test_cache(request)


	profile = Profile.objects.get(user=request.user)


	work_id = profile.work_id

	# return HttpResponseRedirect('/')
	if work_id:
		return HttpResponse("评分功能只针对学生用户, 教师用户请返回")



	teachers =  Teacher2.objects.all()
	# for t in teachers:
	# 	print "here is teacher %s, name %s" %(t.tid, t.name)
 
	score_contents = list()
	for i in RatingItem.objects.all():
		score_contents.append(i.content)
	

	def getKey(custom):
		return custom.id

	score_contents = sorted(RatingItem.objects.all(), key=getKey)
	# for i in score_contents:
	# 	print i
	template = "rating.html"

	if int(id):
		first_t = Teacher2.objects.get(id=id)	
	else:
		first_t = ''	
	context = {"username": user, 
				"email": email,
				"teachers": teachers,
				"score_contents": score_contents,
				"first_t": first_t
				}


	return render(request, template, context)


def redirect(request):
	print "here is redirect"
	template = "redirect_nosignin.html"

	context = {
				}


	return render(request, template, context)

def success_redirect(request, tid):
	template = "success_redirect.html"

	context = {"tid" : tid,
				}


	return render(request, template, context)

import uuid 
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = User.objects.get(ref_id=ref_id)
		return id_exists
	except:
		return ref_id

@cache_page(5)
def test_cache(request):
	return HttpResponse("hello")


def check_rater(request, tid):
	user = request.user.username
	email = request.user.email
	teacher = Teacher2.objects.get(id=tid)
	print teacher.score_rater
	print "hererere"
	if user in json.loads(teacher.score_rater):
		print "in here"
		return HttpResponse("<p>您已对该教师进行过评分</p>")
	else:
		teachers =  Teacher2.objects.all()
	# for t in teachers:
	# 	print "here is teacher %s, name %s" %(t.tid, t.name)
		template = "rating_form.html"

		score_contents = list()
		for i in RatingItem.objects.all():
			score_contents.append(i.content)
	

		def getKey(custom):
			return custom.id



		score_contents = sorted(RatingItem.objects.all(), key=getKey)

		context = {
					"score_contents": score_contents
					}


	return render(request, template, context)




