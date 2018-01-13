from django.db.models.signals import post_save,post_delete, post_migrate
from django.core.signals import request_started
from django.dispatch import receiver
import logging

from .models import Student, Group



@receiver(post_save, sender = Student)
def log_student_updated_added_event(sender,**kwargs):
	logger = logging.getLogger(__name__)

	student = kwargs['instance']
	if kwargs['created']:
		logger.info("Student added: %s %s (ID: %d)", student.first_name,student.last_name,student.id)
	else:
		logger.info("Student updated: %s %s (ID: %d)", student.first_name,student.last_name,student.id)



@receiver(post_delete, sender = Student)
def log_student_deleted_event(sender,**kwargs):
	logger = logging.getLogger(__name__)

	student = kwargs['instance']
	logger.info("Student deleted: %s %s (ID: %d)",student.first_name,student.last_name,student.id)



@receiver(post_save, sender = Group)
def log_group_updated_added_event(sender,**kwargs):
	logger = logging.getLogger(__name__)

	group = kwargs['instance']
	if kwargs['created']:
		logger.info("Group added: %s (ID: %d)", group.name, group.id)
	else:
		logger.info("Group updated: %s (ID: %d)", group.name,group.id)




@receiver(post_delete, sender = Group)
def log_group_deleted_event(sender,**kwargs):
	logger = logging.getLogger(__name__)

	group = kwargs['instance']
	logger.info("Group deleted: %s (ID: %d)", group.name,group.id)



def Numb():
	try:
		Numb.number_of_requests +=1
	except AttributeError:
		Numb.number_of_requests = 1
	return Numb.number_of_requests

@receiver(request_started)
def log_request_started_calculate_event(sender,**kwargs):
	logger = logging.getLogger(__name__)
	logger.info("Request number (%d)", Numb())

