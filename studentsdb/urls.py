from django.conf.urls import include, patterns, url
#from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.packets.students import StudentUpdateView, StudentDeleteView
from students.packets.journal import JournalView
from django.views.generic import RedirectView, TemplateView
from students.packets.groups import GroupsUpdateView, GroupsDeleteView
from students.packets.profile import ProfileUpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
import django


js_info_dict = {
    'packages':('students',),
}


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentsdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Students urls
    url(r'^$', 'students.packets.students.students_list', name='home'),
    url(r'^students/add/$','students.packets.students.students_add', name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),


    #Groups urls 
    url(r'^groups/$', 'students.packets.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.packets.groups.groups_add', name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupsUpdateView.as_view(), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupsDeleteView.as_view(), name='groups_delete'),

    url(r'^journal/(?P<pk>\d+)?/?$',login_required(JournalView.as_view()), name='visitation'),

    #User related urls
    url(r'^users/logout/$',auth_views.logout,kwargs={'next_page':'home'},name = 'logout'),
    url(r'^register/complete/$',RedirectView.as_view(pattern_name='home'),name= 'registration_complete'),
    url(r'^users/profile/$',login_required(TemplateView.as_view(template_name='registration/profile.html')),name='profile'),
    url(r'^users/profile_edit/(?P<pk>\d+)/$', login_required(ProfileUpdateView.as_view()), name='profile_edit'),
    url(r'^users/',include('registration.backends.simple.urls',namespace='users')),

    url('',include('social.apps.django_app.urls',namespace='social')),

    url(r"^contact-admin/$", 'students.packets.contact_admin.contact_admin', name='contact_admin'),

    url(r'^jsi18n\.js$','django.views.i18n.javascript_catalog',js_info_dict),


    url(r'^admin/', include(django.contrib.admin.site.urls)),
)

if DEBUG:
    urlpatterns+=patterns('',
        url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':MEDIA_ROOT}))	
