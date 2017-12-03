# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def groups_list(request):
	groups = (
		{'id':1,
		 'name': u'TA-51',
		 'leader': u'Ваниш Изи'},
		{'id':2,
		  'name': u'TO-51',
		  'leader': u'Хата зе-Биг'},
		{'id':3,
		 'name': u'TO-61',
		 'leader': u'Богдан Иванов'}
		)
	return render(request, 'students/groups_list.html', {'groups' : groups})




# Views for groups

def groups_edit(request,gid):
	return HttpResponse('<h1>Groups Edit %s</h1>' %gid)

def groups_add(request):
	return HttpResponse('<h1>Group Add </h1>')

def groups_delete(request, gid):
	return HttpResponse('<h1>Group Delete %s</h1>' %gid)
