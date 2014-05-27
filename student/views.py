# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.list import ListView, MultipleObjectMixin
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from django.db import models
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from course.views import elected_course, cancel_elected
from course.models import ElectedCourse, OpenCourse, SiteSettings

import re

from django.contrib import messages
# Create your views here.

ss = SiteSettings.objects.filter()
current_semester = ss[0].current_semester

class MixinByStudent(MultipleObjectMixin):
    def get_queryset(self):
        user = self.request.user
        queryset = super(MixinByStudent, self).get_queryset()
        queryset_by_student = queryset.filter(student=user)
        return queryset_by_student

class ElectedCourseListView(ListView,MixinByStudent):
    model = ElectedCourse
    template_name = 'student/elected_course_list.tpl'
    context_object_name = 'elected_course_list'

    def get_queryset(self):
        queryset = super(ElectedCourseListView,self).get_queryset()
        queryset = queryset.filter(course__semester=current_semester)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ElectedCourseListView,self).get_context_data(**kwargs)
        elected_course = context['elected_course_list']
        week_list = {u'一':'',
                     u'二':'',
                     u'三':'',
                     u'四':'',
                     u'五':'',
                     }
        week = [week_list.copy(),week_list.copy(),week_list.copy(),
                week_list.copy(),week_list.copy(),week_list.copy(),
                week_list.copy(),week_list.copy(),week_list.copy(),
                week_list.copy(),week_list.copy(),week_list.copy(),
                week_list.copy(),]

        day_pattern = re.compile(u'[一二三四五]\d{1,2}-\d{1,2}') # find the time
        hour_pattern = re.compile(r'\d{1,2}')
        for course in elected_course:
            course_time = day_pattern.findall(course.course.time) or []
            for day_time in course_time:
                hours = hour_pattern.findall(day_time)
                for hour in xrange(int(hours[0])-1,int(hours[1])):
                    week[hour][day_time[0]] = course.course.course.name
            # import code;code.interact(local=locals())
        context['week'] = week
        return context

class CurrentCourseScoreListView(ListView,MixinByStudent):
    model = ElectedCourse
    template_name = "student/current_score_list.tpl"
    context_object_name = "courses"

    def get_queryset(self):
        queryset = super(CurrentCourseScoreListView,self).get_queryset()
        queryset_by_semester = queryset.filter(course__semester=current_semester)
        return queryset_by_semester

    def get_context_data(self, **kwargs):
        context = super(CurrentCourseScoreListView,self).get_context_data(**kwargs)
        courses = context["courses"]
        avg_score = courses.aggregate(avg_score=models.Avg("score"))["avg_score"]
        context["avg_score"] = avg_score
        return context


class CourseScoreListView(ListView,MixinByStudent):
    model = ElectedCourse
    template_name = "student/score_list.tpl"
    context_object_name = "courses"

    def get_context_data(self, **kwargs):
        context = super(CourseScoreListView,self).get_context_data(**kwargs)
        courses = context["courses"]
        avg_score = courses.aggregate(avg_score=models.Avg("score"))["avg_score"]
        context["avg_score"] = avg_score
        return context

@login_required
def student_elected_course(request):
    '''选课'''
    if request.method == "POST":
        user = request.user
        course_list = request.POST.getlist("open_course") or []
        elected_course(request,user,course_list)
        return HttpResponseRedirect(reverse('open_course_list'))
    else :
        return HttpResponseForbidden()

@login_required
def student_cancel_elected(request):
    if request.method == "POST":
        user = request.user
        course_list = request.POST.getlist("open_course") or []
        cancel_elected(request,user,course_list)
        return HttpResponseRedirect(reverse('elected_course'))
    else :
        return HttpResponseForbidden()
