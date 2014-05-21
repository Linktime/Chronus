from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.views import login

from course.views import dblogout, index
from course.views import OpenCourseListView, CourseListView

from student import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/',login,{'template_name':'login.tpl'},name="login"),
    url(r'^logout/$',dblogout,name="logout"),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^course/$',CourseListView.as_view()),
    url(r'^open_course/$',OpenCourseListView.as_view(),name="open_course_list"),

    url(r'^student/',include('student.urls')),
)
