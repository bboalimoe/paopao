#coding=utf-8

#从django.http模块中导入HttpResponse类[1]
from django.shortcuts import render_to_response


# from mysite.books.models import Book

def hello(request):
    """ get user name of the system and say hello.

    tested under ubuntu 12.04"""

    import commands
    user = commands.getstatusoutput('echo $USER')[1]
    return render_to_response('sample.html', {'name': user})
