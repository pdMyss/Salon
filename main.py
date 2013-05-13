#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response

def menu(fam):
    return render_to_response('menu.html')

def list1(request):
    return render_to_response('list1.html')

 