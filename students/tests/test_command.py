from django.test import TestCase
from django.core.management import call_command
from django.utils.six import StringIO



class STCountTest(TestCase):


	def setUp(self):
		group1,created = Group.objects.get_or_create(id=1,name="Group1")
		group2,created = Group.objects.get_or_create(id=2,name="Group2")

		Student.objects.get_or_create(id=1,first_name ='first',last_name ='1',birthday=datetime.today(),ticket='1',student_group=group1)
		Student.objects.get_or_create(id=2,first_name ='second',last_name ='2',birthday=datetime.today(),ticket='2',student_group=group1)
		Student.objects.get_or_create(id=3,first_name ='third',last_name ='3',birthday=datetime.today(),ticket='3',student_group=group1)
		Student.objects.get_or_create(id=4,first_name ='forth',last_name ='4',birthday=datetime.today(),ticket='4',student_group=group2)
		Student.objects.get_or_create(id=5,first_name ='fifth',last_name ='5',birthday=datetime.today(),ticket='5',student_group=group2)
		Student.objects.get_or_create(id=6,first_name ='sixth',last_name ='6',birthday=datetime.today(),ticket='6',student_group=group2)


	def test_command_output(self):
		out = StringIO()
		call_command('stcount','student','group','user',stdout=out)
		result = out.getvalue()

		self.assertIn('students in database: 6',result)
		self.assertIn('groups in database: 2',result)
		self.assertIn('users in database: 5',result)


