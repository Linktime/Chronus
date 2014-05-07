from django.conf.urls import patterns, include, url

from student.ajaxs import ajax_student_elected_course

from student.views import ElectedCourseListView

urlpatterns = patterns('',
    url(r'^elected_course/$',ElectedCourseListView.as_view(),name='student_elected_course'),

    url(r'^ajax/elected_course/$',ajax_student_elected_course)
)