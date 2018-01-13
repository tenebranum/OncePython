from django.conf.urls import include, patterns, url
#from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.packets.students import StudentUpdateView, StudentDeleteView
from students.packets.journal import JournalView
from students.packets.groups import GroupsUpdateView, GroupsDeleteView
import django

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

    url(r'^journal/(?P<pk>\d+)?/?$',JournalView.as_view() , name='visitation'),
    url(r'^journal/(?P<pk>\d+)/edit/$', 'students.packets.visitation.visitation_edit', name='visitation_edit'),

    url(r"^contact-admin/$", 'students.packets.contact_admin.contact_admin', name='contact_admin'),


    url(r'^admin/', include(django.contrib.admin.site.urls)),
)

if DEBUG:
    urlpatterns+=patterns('',
        url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':MEDIA_ROOT}))	
