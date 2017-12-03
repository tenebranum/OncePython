from django.conf.urls import include, patterns, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentsdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Students urls
    url(r'^$', 'students.packets.students.students_list', name='home'),
    url(r'^students/add/$','students.packets.students.students_add', name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', 'students.packets.students.students_edit', name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', 'students.packets.students.students_delete', name='students_delete'),


    #Groups urls 
    url(r'^groups/$', 'students.packets.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.packets.groups.groups_add', name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.packets.groups.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.packets.groups.groups_delete', name='groups_delete'),

    url(r'^visitation/$', 'students.packets.visitation.visitation_list', name='visitation'),
    url(r'^visitation/(?P<vid>\d+)/edit/$', 'students.packets.visitation.visitation_edit', name='visitation_edit'),


    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    urlpatterns+=patterns('',
        url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':MEDIA_ROOT}))	
