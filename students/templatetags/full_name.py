from django import template
from django.contrib.auth.models import User


register = template.Library()


@register.filter
def full_name(user):
	result = ''
	if user.first_name and user.last_name:
		result = ' '.join((user.first_name,user.last_name))
	else:
		result = user.username
	return result
