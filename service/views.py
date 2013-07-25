#coding=utf-8

#从django.http模块中导入HttpResponse类[1]
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response('home.html', RequestContext(request))
