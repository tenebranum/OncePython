from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import RequestContext, loader
from ..models import Student
from ..util import paginate, get_current_group
from django.views.generic import UpdateView, DeleteView, DetailView
from django.forms import ModelForm, ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions



class ProfileUpdateForm(ModelForm):


	class Meta:
		model = User
		fields = ['email','username','first_name','last_name']


	password = forms.CharField(label=_(u'Password'),widget=forms.PasswordInput(),initial="")


	def save(self, user = None):
		user_profile = super ( ProfileUpdateForm,self ).save(commit=False)
		user_profile.set_password(self.cleaned_data['password'])
		user_profile.save()
		return user_profile

	def __init__(self,*args,**kwargs):

		super(ProfileUpdateForm,self).__init__(*args,**kwargs)
		self.helper = FormHelper(self)
		self.helper.action = reverse('profile_edit', kwargs = {'pk':kwargs['instance'].id})
		self.helper.method = 'GET'
		self.helper.form_class = 'form-horizontal'
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.field_class = 'col-sm-10'
		self.helper.label_class = 'col-sm-2 control-label'

		self.helper.layout[0] = FormActions(
			Submit('add_button',_(u'Save'),css_class='btn btn-primary'),
			Submit('cancel_button',_(u'Cancel'),css_class='btn btn-link')
			)


class ProfileUpdateView(UpdateView):
	model = User
	template_name = "registration/profile_edit.html"
	form_class = ProfileUpdateForm


	def get_success_url(self):
		return u'%s?status_message=%s' % ( reverse('home'),_(u'Changes have been saved'))

	def post(self,request,*args,**kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=%s' % ( reverse('home'),_(u'Changes have been canceled')))
		else:
			return super(ProfileUpdateView,self).post(request,*args,**kwargs)



