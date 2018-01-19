from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class StProfile(models.Model):
	user = models.OneToOneField(User)

	class Meta(object):
		verbose_name = _(u"User Profile")

	mobile_phone = models.CharField(max_length=12,default='',verbose_name = _(u"Mobile Phone"))

	home_address = models.CharField(max_length=50, default='', blank=False, null = True, verbose_name = _(u"Home Address"))




	def __unicode__(self):
		return self.user.username
