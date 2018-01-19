from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.



class Student(models.Model):

	class Meta(object):
		verbose_name=_(u"Student")
		verbose_name_plural=_(u"Students")

	first_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=_(u'Name'))

	last_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=_(u'Surname'))

	middle_name = models.CharField(
		max_length=256,
		blank=True,
		verbose_name=_(u'Middle name'),
		default='')

	birthday = models.DateField(
		blank=False,
		null=True,
		verbose_name=_(u'Birthday'))

	photo = models.ImageField(
		blank=True,
		verbose_name=_(u'Photo'),
		null=True)

	ticket = models.CharField(
		max_length=256,
		verbose_name=_(u'Student ticket'),
		blank=False)

	notes=models.TextField(
		blank=True,
		verbose_name=_(u'Notes'),
		null=True)

	student_group = models.ForeignKey('Group',
		verbose_name=_(u'Group'),
		blank=False,
		null=True,
		on_delete=models.PROTECT)
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Group(models.Model):

	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=_(u'Title'))

	leader = models.OneToOneField('Student',
		verbose_name=_(u'Leader'),
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	notes=models.TextField(
		blank=True,
		verbose_name=_(u'Notes'),
		null=True)
	def __unicode__(self):
		if self.leader:
			return u'%s (%s %s)' % (self.name, self.leader.first_name, self.leader.last_name)
		else:
			return u'%s' % (self.name)



class MonthJournal(models.Model):


	class Meta:
		verbose_name = _(u'Month journal')
		verbose_name_plural=_(u"Month journals")


	student = models.ForeignKey('Student',verbose_name=_(u'Students'),blank=False,unique_for_month='date')
	date = models.DateField(verbose_name=_(u'Date'),blank=False)
	days = []
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

	def __init__(self,*args,**kwargs):
		super(MonthJournal,self).__init__(*args,**kwargs)
		for i in range(1,32):
			self.days.append(False)