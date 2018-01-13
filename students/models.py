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



class MonthJournal(models.Model):


	class Meta:
		verbose_name = u'Месячный журнал'
		verbose_name_plural = u'Месячные журналы'


	student = models.ForeignKey('Student',verbose_name=u'Студент',blank=False,unique_for_month='date')
	date = models.DateField(verbose_name=u'Дата',blank=False)
	present_day1 = models.BooleanField(default=False)
	present_day2 = models.BooleanField(default=False)
	present_day3 = models.BooleanField(default=False)
	present_day4 = models.BooleanField(default=False)
	present_day5 = models.BooleanField(default=False)
	present_day6 = models.BooleanField(default=False)
	present_day7 = models.BooleanField(default=False)
	present_day8 = models.BooleanField(default=False)
	present_day9 = models.BooleanField(default=False)
	present_day10 = models.BooleanField(default=False)
	present_day11 = models.BooleanField(default=False)
	present_day12 = models.BooleanField(default=False)
	present_day13 = models.BooleanField(default=False)
	present_day14 = models.BooleanField(default=False)
	present_day15 = models.BooleanField(default=False)
	present_day16 = models.BooleanField(default=False)
	present_day17 = models.BooleanField(default=False)
	present_day18 = models.BooleanField(default=False)
	present_day19 = models.BooleanField(default=False)
	present_day20 = models.BooleanField(default=False)
	present_day21 = models.BooleanField(default=False)
	present_day22 = models.BooleanField(default=False)
	present_day23 = models.BooleanField(default=False)
	present_day24 = models.BooleanField(default=False)
	present_day25 = models.BooleanField(default=False)
	present_day26 = models.BooleanField(default=False)
	present_day27 = models.BooleanField(default=False)
	present_day28 = models.BooleanField(default=False)
	present_day29 = models.BooleanField(default=False)
	present_day30 = models.BooleanField(default=False)
	present_day31 = models.BooleanField(default=False)


	def __unicode__(self):
		return u'%s: %d , %d' % (self.student.last_name, self.date.month, self.date.year)