from django.test import TestCase
from django.http import HttpRequest

from students.models import Student,Group 
from students.util import get_current_group, get_groups, paginate



class UtilsTestCase(TestCase):

	def setUp(self):
		group1 = Group.objects.get_or_create(id=1,name="Group1")
		group2 = Group.objects.get_or_create(id=2,name="Group2")
		group3 = Group.objects.get_or_create(id=3,name="Group3")


	def test_get_current_group(self):
		request = HttpRequest()
		
		request.COOKIES['current_group']=''
		self.assertEqual(None,get_current_group(request))

		request.COOKIES['current_group']='12345'
		self.assertEqual(None,get_current_group(request))

		group = Group.objects.filter(name='Group1')[0]
		request.COOKIES['current_group']=str(group.id)
		self.assertEqual(group,get_current_group(request))


	def test_get_groups(self):
		request = HttpRequest()

		request.COOKIES['current_group']=''

		self.assertEqual(3,len(get_groups(request)))
		for gr in get_groups(request):
			self.assertEqual(False,gr['selected'])

		request.COOKIES['current_group']= Group.objects.count()
		self.assertEqual(True,get_groups(request)[-1]['selected'])


	def test_paginate(self):
		request = HttpRequest()
		request.GET._mutable = True
		request.GET['page']=2

		objects = Group.objects.all()
		size = 2
		context = {}
		var_name = 'list'

		self.assertEqual(1,len(paginate(objects,size,request,context,var_name)['list']))

		size = 3

		self.assertEqual(False,paginate(objects,size,request,context,var_name)['is_paginated'])


