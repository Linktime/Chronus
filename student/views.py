# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.list import ListView, MultipleObjectMixin
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from course.models import ElectedCourse, OpenCourse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

import re

from django.contrib import messages
# Create your views here.

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
                for hour in xrange(int(hours[0]),int(hours[1])+1):
                    week[hour][day_time[0]] = course.course.course.name
            # import code;code.interact(local=locals())
        context['week'] = week
        return context

@login_required
def elected_course(request):
    '''选课'''
    if request.method == "POST":
        user = request.user
        course_list = request.POST.getlist("open_course") or []
        for course_id in course_list:
            course = OpenCourse.objects.get(id=course_id)
            try :
                elected_course = ElectedCourse.objects.get(student=user,course=course)
                messages.warning(request,u"课程《%s》已经选取，请不要重复选课！"%course.course.name)
            except ElectedCourse.DoesNotExist :
                elected_course = ElectedCourse(student=user,course=course)
                old_elected_course = ElectedCourse.objects.filter(student=user)
                day_pattern = re.compile(u'[一二三四五]\d{1,2}-\d{1,2}') # find the time
                hour_pattern = re.compile(r'\d{1,2}')

                new_course_time = day_pattern.findall(elected_course.course.time)
                new_course_dict = {}
                for single in new_course_time:
                    new_course_dict[single[0]] = [int(x) for x in hour_pattern.findall(single)]

                flag = True

                for old_course in old_elected_course:
                    course_time = day_pattern.findall(old_course.course.time) or []
                    for day_time in course_time:
                        if day_time[0] in new_course_dict.keys():
                            hours = hour_pattern.findall(day_time)
                            hours_list = range(int(hours[0]),int(hours[1])+1)
                            common = list(set(new_course_dict[day_time[0]]).intersection(set(hours_list)))
                            if common:
                                flag = False

                if flag:
                    elected_course.save()
                    messages.success(request,u"课程《%s》选课成功，你可以继续选择其它课程！"%course.course.name)
                else:
                    messages.warning(request,u"课程《%s》选课失败，请确认选课时间是否冲突！"%course.course.name)

        return HttpResponseRedirect(reverse('open_course_list'))
    else :
        return HttpResponseForbidden()

@login_required
def cancel_elected(request):
    if request.method == "POST":
        user = request.user
        course_list = request.POST.getlist("open_course") or []
        for course_id in course_list:
            course = OpenCourse.objects.get(id=course_id)
            try :
                elected_course = ElectedCourse.objects.get(student=user,course=course)
                elected_course.delete()
                messages.success(request,u"课程《%s》退课成功，你可以继续选择其它课程或者退课！"%course.course.name)
            except ElectedCourse.DoesNotExist :
                messages.warning(request,u"课程《%s》还未选取！"%course.course.name)
        return HttpResponseRedirect(reverse('student_elected_course'))
    else :
        return HttpResponseForbidden()
