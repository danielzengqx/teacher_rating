# -*- coding: utf-8 -*-
# coding=gbk
# from __future__ import absolute_import

from django.conf import settings 
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
# from models import Huodong, Info, UserHuodong
import sys
from django.core.cache import cache
from collections import OrderedDict


from django.views.decorators.csrf import csrf_exempt
from lxml import etree
import hashlib
# import requests


def checkSignature(request):
    signature = request.GET.get('signature',None)
    timestamp = request.GET.get('timestamp',None)
    nonce = request.GET.get('nonce',None)
    echostr = request.GET.get('echostr',None)
    
    token = "momoking"

    tmplist = [token,timestamp,nonce]
    tmplist.sort()
    tmpstr = "%s%s%s"%tuple(tmplist)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    if tmpstr == signature:
        return echostr
    else:
        return None

@csrf_exempt
def weixin(request):
	try:
	    if request.method == 'GET':
	    	print request
	       	response = HttpResponse(checkSignature(request))
	       	return response

	    elif request.method ==  'POST':
	    	print "daniel ,here is post!"
	    	print request.body
	    	str_xml = request.body #get post data 
	    	xml = etree.fromstring(str_xml) #parse xml
	    	print xml


	    	msgType = xml.find("MsgType").text
	    	fromUser = xml.find("FromUserName").text
	    	toUser = xml.find("ToUserName").text

	    	vl_title1 = "教师评分系统"
	    	vl_description1 = "教师评分系统"
	    	# vl_pic_url1 = "http://b87.photo.store.qq.com/psb?/V117jtH91i6nzd/*iBbJ98RLScbg*EF4QwUsi3rYA1zWHBJYq*hw6qM3a4!/b/dODm6DPGfAAA&bo=ngK*AQAAAAABAAU!&rf=viewer_4&t=5"
	    	vl_pic_url1 = "http://www.xiaoxiezi.net/static/assets/images/03.jpg"
	    	vl_url1 = "http://www.xiaoxiezi.net/"

	    	vl_title = "教师评分系统"
	    	vl_description = "教师评分系统"
	    	# vl_pic_url = "http://b88.photo.store.qq.com/psb?/V117jtH91i6nzd/a2xngiBE0QvjwOHbXEi4kltiOhcn59l1Qm9pgpuR*pA!/b/dLpIdTT5SAAA&bo=ngK.AQAAAAABAAQ!&rf=viewer_4&t=5"
	    	vl_pic_url = "http://www.xiaoxiezi.net/static/assets/images/03.jpg"
	    	vl_url = "http://www.xiaoxiezi.net/"								
                                
            response = "<xml>\
			            <ToUserName><![CDATA[" + fromUser + "]]></ToUserName>\
			            <FromUserName><![CDATA[" + toUser + "]]></FromUserName>\
			            <CreateTime>12345678</CreateTime>\
			            <MsgType><![CDATA[news]]></MsgType>\
			            <ArticleCount>2</ArticleCount>\
			            <Articles>\
			            <item>\
			            <Title><![CDATA[" + vl_title1 + "]]></Title> \
			            <Description><![CDATA[" + vl_description1 + "]]></Description>\
			            <PicUrl><![CDATA[" + vl_pic_url1 + "]]></PicUrl>\
			            <Url><![CDATA[" + vl_url1 + "]]></Url>\
			            </item>\
			            <item>\
			            <Title><![CDATA[" + vl_title + "]]></Title>\
			            <Description><![CDATA[" + vl_description + "]]></Description>\
			            <PicUrl><![" + vl_pic_url + "]]></PicUrl>\
			            <Url><![CDATA[" + vl_url + "]]></Url>\
			            </item>\
			            </Articles>\
			            </xml>"
            return HttpResponse(response)

      #   else:
	    	# print "here is else %s" % request
	     #    return HttpResponse('Hello World')

	except Exception, error: #to print the error
		print error


def mx(request):
	template = "snow.html"
	context = {}
	return render(request, template, context)
