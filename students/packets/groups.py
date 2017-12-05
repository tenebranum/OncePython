# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import RequestContext, loader
from ..models import Group, Student

def groups_list(request):
	groups = Group.objects.all()
	order_by = request.GET.get('order_by','')
	if order_by in ('name','id'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse','') == '1' :
			groups = groups.reverse()
	else:
		groups = groups.order_by('name')

	paginator = Paginator( groups, 2)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		groups = paginator.page(1)
	except EmptyPage:
		groups = paginator.page(paginator.num_pages)

	return render(request, 'students/groups_list.html', {'groups' : groups})




# Views for groups

def groups_edit(request,gid):
	return HttpResponse('<h1>Groups Edit %s</h1>' %gid)

def groups_add(request):
	return HttpResponse('<h1>Group Add </h1>')

def groups_delete(request, gid):
	return HttpResponse('<h1>Group Delete %s</h1>' %gid)
