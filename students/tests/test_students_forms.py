from django.test import TestCase,Client,override_settings
from django.core.urlresolvers import reverse 
from students.models import Group,Student
from datetime import datetime

@override_settings(LANGUAGE_CODE='en')
class TestStudentUpdateForm(TestCase):

	def setUp(self):
		group1,created = Group.objects.get_or_create(id=1,name="Group1")
		group2,created = Group.objects.get_or_create(id=2,name="Group2")

		Student.objects.get_or_create(id=1,first_name ='first',last_name ='1',birthday=datetime.today(),ticket='1',student_group=group1)
		Student.objects.get_or_create(id=2,first_name ='second',last_name ='2',birthday=datetime.today(),ticket='2',student_group=group1)
		Student.objects.get_or_create(id=3,first_name ='third',last_name ='3',birthday=datetime.today(),ticket='3',student_group=group1)
		Student.objects.get_or_create(id=4,first_name ='forth',last_name ='4',birthday=datetime.today(),ticket='4',student_group=group2)
		Student.objects.get_or_create(id=5,first_name ='fifth',last_name ='5',birthday=datetime.today(),ticket='5',student_group=group2)
		Student.objects.get_or_create(id=6,first_name ='sixth',last_name ='6',birthday=datetime.today(),ticket='6',student_group=group2)


		self.client=Client()
		self.url=reverse("students_edit",kwargs={'pk':1})


	def test_form(self):
		self.client.login(username='tenebranum',password='kava98banga')

		response = self.client.get(self.url,follow=True)

		self.assertEqual(response.status_code,200)
		self.assertIn('Student ticket*', response.content)
		self.assertIn('Surname*', response.content)
		self.assertIn('name="add_button"', response.content)
		self.assertIn('name="cancel_button"', response.content)
		self.assertIn('action="%s"' % self.url, response.content)

	def test_success(self):
		self.client.login(username="tenebranum",password="kava98banga")
		group = Group.objects.filter(name="Group2")[0]
		response = self.client.post(self.url,{'first_name':'updated name',
											  'last_name':'updated last name',
											  'ticket':'566',
											  'student_group':group.id,
											  'birthday':'1990-10-11'},follow=True)
		self.assertEqual(response.status_code,200)

		student = Student.objects.get(pk=1)
		self.assertEqual(student.first_name,'updated name')
		self.assertEqual(student.last_name,'updated last name')
		self.assertEqual(student.ticket,'566')
		self.assertEqual(student.student_group,group)

		self.assertIn('Student updated successfully',response.content)
		self.assertEqual(response.redirect_chain[0][0],'http://testserver/?status_message='+'Student%20updated%20successfully!')


	def test_access(self):
		response = self.client.get(self.url,follow=True)

		self.assertEqual(response.status_code,200)
		self.assertIn('Login Form',response.content)
		self.assertEqual(response.redirect_chain[0],('http://testserver/users/login/?next=/students/1/edit/',302))
