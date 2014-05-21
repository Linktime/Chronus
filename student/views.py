# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.list import ListView, MultipleObjectMixin
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from course.models import ElectedCourse, OpenCourse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

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
                elected_course.save()
                messages.success(request,u"课程《%s》选课成功，你可以继续选择其它课程！"%course.course.name)
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
