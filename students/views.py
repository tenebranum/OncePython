# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Views for students
def students_list(request):
	students = (
		{'id':1,
		 'first_name': u'Хата',
		 'last_name': u'зе-Биг',
		 'ticket': u'666',
		 'image': 'img/Хата.jpg'},
		 {'id':2,
		  'first_name': u'Ваниш',
		  'last_name': u'Изи',
		  'ticket': u'111',
		  'image': 'img/Ваниш.jpg'},
		 {'id':3,
		  'first_name': u'Богдан',
		  'last_name': u'Иванов',
		  'ticket': u'123',
		  'image': 'img/Хата.jpg'}
		 )
	return render(request, 'students/students_list.html', {'students': students})



# Views for groups
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


def students_add(request):
	return HttpResponse('<h1>Add Student</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' %sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' %sid)

# Views for groups

def groups_edit(request,gid):
	return HttpResponse('<h1>Groups Edit %s</h1>' %gid)

def groups_add(request):
	return HttpResponse('<h1>Group Add </h1>')

def groups_delete(request, gid):
	return HttpResponse('<h1>Group Delete %s</h1>' %gid)
# Create your views here.
