#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from infa.models import Name, People

def save(fio):
    n = Name.object.create(name=fio)
    n.save()

def menu(request):
    p = People.objects.all()
    if request.method == 'POST':
        fio = request.REQUEST['fio']
        save(fio)
    return render_to_response('menu.html')    

def list1(request):
    return render_to_response('list1.html')
 