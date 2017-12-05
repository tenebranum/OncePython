# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.



class Student(models.Model):

	first_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u'Имя')

	last_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u'Фамилия')

	middle_name = models.CharField(
		max_length=256,
		blank=True,
		verbose_name=u'Отчество',
		default='')

	birthday = models.DateField(
		blank=False,
		null=True,
		verbose_name=u'Дата рождения')

	photo = models.ImageField(
		blank=True,
		verbose_name=u'Фото',
		null=True)

	ticket = models.CharField(
		max_length=256,
		verbose_name=u'Билет',
		blank=False)

	notes=models.TextField(
		blank=True,
		verbose_name=u'Дополнительные сведения',
		null=True)

	student_group = models.ForeignKey('Group',
		verbose_name=u'Группа',
		blank=False,
		null=True,
		on_delete=models.PROTECT)
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Group(models.Model):

	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u'Название')

	leader = models.OneToOneField('Student',
		verbose_name=u'Староста',
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	notes=models.TextField(
		blank=True,
		verbose_name=u'Дополнительные сведения',
		null=True)
	def __unicode__(self):
		if self.leader:
			return u'%s (%s %s)' % (self.name, self.leader.first_name, self.leader.last_name)
		else:
			return u'%s' % (self.name)