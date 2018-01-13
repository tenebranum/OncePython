# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from ..models import Student, Group
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib import messages
from django.forms import ModelForm
from ..util import paginate, get_current_group
from django.views.generic import UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

def students_list(request):
	current_group = get_current_group(request)
	if current_group:
		students = Student.objects.filter(student_group=current_group)
	else:
		students = Student.objects.all()
	#sort students
	order_by = request.GET.get('order_by','')
	if order_by in ('last_name', 'first_name', 'ticket','id'):
		students = students.order_by(order_by)
		if request.GET.get('reverse','') == '1':
			students = students.reverse()
	else: 
		students = students.order_by('last_name')

	#paginate students	
	context = paginate(students,3,request,{},var_name='students')

	return render(request, 'students/students_list.html', context)




def students_add(request):

	if request.method == 'POST':
		if request.POST.get('add_button') is not None:
			#TODO
			errors={}

			data = {'middle_name':request.POST.get('middle_name'),
					'notes':request.POST.get('notes')}

			first_name=request.POST.get('first_name','').strip()
			if not first_name:
				errors['first_name']=u'Имя является обязательным'
			else:
				data['first_name']=first_name

			last_name=request.POST.get('last_name','').strip()
			if not last_name:
				errors['last_name']=u'Фамилия является обязательной'
			else:
				data['last_name']=last_name

			ticket=request.POST.get('ticket','').strip()
			if not ticket:
				errors['ticket']=u'Билет является обязательным'
			else:
				data['ticket']=ticket

			birthday=request.POST.get('birthday','').strip()
			if not birthday:
				errors['birthday']=u'Дата рождения является обязательной'
			else:
				try:
					datetime.strptime(birthday, '%Y-%m-%d')
				except Exception:
					errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
				else:
					data['birthday'] = birthday

			photo=request.FILES.get('photo')
			if photo:
				data['photo']=photo

			student_group=request.POST.get('student_group','').strip()
			if not student_group:
				errors['student_group']=u'Выберите группу'
			else:
				student_group = Group.objects.get(pk=student_group)
				data['student_group']=student_group

			if not errors:
				student=Student(**data)
				student.save()
				return HttpResponseRedirect(
					u'%s?status_message=Студент успешно добавлен'%
					reverse('home'))

			else:
				messages.success	(request, u'Ошибка при вводе данных')
				return render(request,'students/students_add.html',{'groups':Group.objects.all().order_by('name'),
																	'errors':errors})

		elif request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect(
				u'%s?status_message=Изменения отменены'%
				reverse('home'))

	else:
		return render(request,'students/students_add.html', {'groups':Group.objects.all().order_by('name')})


class StudentUpdateForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name','last_name','middle_name','birthday','ticket','student_group', 'photo']

	def __init__(self,*args,**kwargs):
		super(StudentUpdateForm,self).__init__(*args,**kwargs)
		self.helper = FormHelper(self)

		self.helper.form_action = reverse('students_edit',kwargs={'pk':kwargs['instance'].id})
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		self.helper.layout[-1] = FormActions(
			Submit('add_button',u'Сохранить',css_class='btn btn-primary'),
			Submit('cancel_button',u'Отменить',css_class='btn btn-link')
			)


class StudentUpdateView(UpdateView):
	model = Student
	template_name = 'students/students_edit.html'
	form_class = StudentUpdateForm

	def get_success_url(self):
		return u'%s?status_message=Изменения сохранены' % reverse('home')

	def post(self,request,*args,**kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Изменения отменены' % reverse('home'))
		else:
			return super(StudentUpdateView,self).post(request,*args,**kwargs)



class StudentDeleteView(DeleteView):
	model = Student
	template_name = 'students/students_delete.html'

	def get_success_url(self):
		return u'%s?status_message=Студент успешно удалён' % reverse('home')



def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' %sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' %sid)

