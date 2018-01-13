# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import RequestContext, loader
from ..models import Group, Student
from ..util import paginate, get_current_group
from django.views.generic import UpdateView, DeleteView
from django.forms import ModelForm, ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions


def groups_list(request):
	current_group = get_current_group(request)
	if current_group:
		groups = Group.objects.all().filter(pk=current_group.pk)
	else:
		groups = Group.objects.all()
	order_by = request.GET.get('order_by','')
	if order_by in ('name','id'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse','') == '1' :
			groups = groups.reverse()
	else:
		groups = groups.order_by('name')

	context = paginate(groups,3,request,{},var_name='groups')

	return render(request, 'students/groups_list.html', context)




# Views for groups


class GroupsUpdateForm(ModelForm):
	class Meta:
		model = Group
		fields = '__all__'


	def clean_leader(self):
		group = Group.objects.get(leader=self.instance.leader)
		if group and self.cleaned_data['leader'].first_name != group.leader.first_name:
			raise ValidationError( u'Студент является старостой другой группы', code = 'invalid')

		return self.cleaned_data['leader']



	def __init__(self,*args,**kwargs):

		super(GroupsUpdateForm,self).__init__(*args,**kwargs)

		self.helper = FormHelper(self)
		self.helper.action = reverse('groups_edit', kwargs = {'pk':kwargs['instance'].id})
		self.helper.method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.field_class = 'col-sm-10'
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.layout[-1] = FormActions(
			Submit('save_button',u'Сохранить', css_class = "btn btn-primary"),
			Submit('cancel_button', u'Отменить', css_class = "btn btn-link")
			)



class GroupsUpdateView(UpdateView):
	model = Group 
	form_class = GroupsUpdateForm
	template_name = "students/groups_edit.html"


	def get_success_url(self):
		return u'%s?status_message=Изменения сохранены.' % reverse('home')


	def post (self,request,*args,**kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Изменения отменены.' % reverse('home'))

		else:
			return super(GroupsUpdateView,self).post(request,*args,**kwargs)


class GroupsDeleteView(DeleteView):
	model = Group
	template_name = "students/groups_delete.html"

	def get_success_url(self):
		return u'%s?status_message=Группа удалена.' % reverse('home')






def groups_add(request):
	return HttpResponse('<h1>Group Add </h1>')


