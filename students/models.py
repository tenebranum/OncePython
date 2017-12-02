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
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)
