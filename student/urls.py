from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from student.views import ElectedCourseListView, CurrentCourseScoreListView, CourseScoreListView\
    , student_elected_course, student_cancel_elected

urlpatterns = patterns('',
    url(r'^elected_course/$',login_required(ElectedCourseListView.as_view()),name='elected_course'),
    url(r'^elected_course/elected/$',student_elected_course, name="student_elected_course"),
    url(r'^elected_course/cancel_elected/$',student_cancel_elected, name="student_cancel_elected"),
    url(r'^current_score/$',login_required(CurrentCourseScoreListView.as_view()),name='current_score'),
    url(r'^score/$',login_required(CourseScoreListView.as_view()),name='score'),
)