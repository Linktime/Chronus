from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from student.views import ElectedCourseListView, elected_course, cancel_elected

urlpatterns = patterns('',
    url(r'^elected_course/$',login_required(ElectedCourseListView.as_view()),name='student_elected_course'),
    url(r'^elected_course/elected/$',elected_course, name="elected_course"),
    url(r'^elected_course/cancel_elected/$',cancel_elected, name="cancel_elected"),
)