#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from infa.models import Name, uchet
import datetime

def save(klient, agent, proc, addtime ):
    n = uchet(klient=klient, agent=agent, proc=proc, addtime_date=addtime)
    n.save()

def menu(request):
    if request.method == 'POST':
        klient = request.POST['klient']
        agent = request.POST['agent']
        proc = request.POST['proc']
        select_month = request.POST['select_month']
        select_day = request.POST['select_day']
        hourse = request.POST['hourse']
        minut = request.POST['minut']
        try:
            addtime = datetime.datetime(2013, int(select_month), int(select_day), int(hourse), int(minut))                             
            save(klient, agent, proc, addtime)
        except:
            pass

    p = uchet.objects.all()
    return render_to_response('menu.html', {'infa': p})

def list1(request):
    return render_to_response('list1.html')
 
def java(request):
    return render_to_response('java.html')