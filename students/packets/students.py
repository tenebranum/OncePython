# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import RequestContext, loader
from ..models import Student

def students_list(request):
	students = Student.objects.all()
	#sort students
	order_by = request.GET.get('order_by','')
	if order_by in ('last_name', 'first_name', 'ticket','id'):
		students = students.order_by(order_by)
		if request.GET.get('reverse','') == '1':
			students = students.reverse()
	else: 
		students = students.order_by('last_name')

	#paginate students	
	paginator = Paginator( students, 2)
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		students = paginator.page(1)
	except EmptyPage:
		students = paginator.page(paginator.num_pages)

	return render(request, 'students/students_list.html', {'students': students})




def students_add(request):
	return HttpResponse('<h1>Add Student</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' %sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' %sid)

