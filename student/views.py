# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.list import ListView, MultipleObjectMixin
from django.http import Http404, HttpResponseForbidden
from course.models import ElectedCourse, OpenCourse
from django.contrib.auth.decorators import login_required
# Create your views here.

class MixinByStudent(MultipleObjectMixin):
    def get_queryset(self):
        user = self.request.user
        queryset = super(MixinByStudent, self).get_queryset()
        queryset_by_student = queryset.filter(student=self.request.user)
        return queryset_by_student

class ElectedCourseListView(ListView,MixinByStudent):
    model = ElectedCourse
    template_name = 'student/elected_course_list.tpl'
    context_object_name = 'elected_course_list'

@login_required
def select_course(request):
    '''选课'''
    if request.method == "POST":
        pass
    else :
        return HttpResponseForbidden()