from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Views for students
def students_list(request):
	return render(request, 'students/students_list.html', {})

def students_add(request):
	return HttpResponse('<h1>Add Student</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' %sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' %sid)

# Views for groups
def groups_list(request):
	return HttpResponse('<h1>Groups Listing</h1>')

def groups_edit(request):
	return HttpResponse('<h1>Groups Edit</h1>')

def groups_add(request, gid):
	return HttpResponse('<h1>Group Add %s</h1>' %gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Group Delete %s</h1>' %gid)
# Create your views here.
