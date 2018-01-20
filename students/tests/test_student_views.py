from django.test import TestCase, Client,override_settings
from datetime import datetime
from django.core.urlresolvers import reverse

from students.models import Student,Group

@override_settings(LANGUAGE_CODE='en')
class TestStudentList(TestCase):

	def setUp(self):
		group1,created = Group.objects.get_or_create(id=1,name="Group1")
		group2,created = Group.objects.get_or_create(id=2,name="Group2")

		Student.objects.get_or_create(first_name ='first',last_name ='1',birthday=datetime.today(),ticket='1',student_group=group1)
		Student.objects.get_or_create(first_name ='second',last_name ='2',birthday=datetime.today(),ticket='2',student_group=group1)
		Student.objects.get_or_create(first_name ='third',last_name ='3',birthday=datetime.today(),ticket='3',student_group=group1)
		Student.objects.get_or_create(first_name ='forth',last_name ='4',birthday=datetime.today(),ticket='4',student_group=group2)
		Student.objects.get_or_create(first_name ='fifth',last_name ='5',birthday=datetime.today(),ticket='5',student_group=group2)
		Student.objects.get_or_create(first_name ='sixth',last_name ='6',birthday=datetime.today(),ticket='6',student_group=group2)

		self.client = Client()
		self.url = reverse('home')


	def test_students_list(self):
		response = self.client.get(self.url)

		self.assertEqual(response.status_code,200)
		self.assertIn('first',response.content)
		#self.assertIn(reverse('students_edit',kwargs={'pk':Student.objects.all()[0].id}),response.content)
		self.assertEqual(len(response.context['students']),3)

	def test_current_group(self):
		group = Group.objects.filter(name='Group1')[0]
		self.client.cookies['current_group']=group.id

		response = self.client.get(self.url)

		self.assertEqual(len(response.context['students']),3)

	def test_order_by(self):
		response = self.client.get(self.url,{'order_by':'last_name'})

		students = response.context['students']
		self.assertEqual(students[0].last_name,'1')
		self.assertEqual(students[1].last_name,'2')
		self.assertEqual(students[2].last_name,'3')

		response = self.client.get(self.url,{'order_by':'last_name','reverse':'1'})
		students = response.context['students']
		self.assertEqual(students[0].last_name,'6')
		self.assertEqual(students[1].last_name,'5')
		self.assertEqual(students[2].last_name,'4')