from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView, MultipleObjectMixin
from django.contrib.auth import logout
from django.db.models import Q

from course.models import OpenCourse, Course

def index(request):
    return render_to_response('index.tpl',context_instance=RequestContext(request))

def dblogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

class OpenCourseListView(ListView):
    model = OpenCourse
    template_name = "open_course_list.tpl"
    context_object_name = "open_courses"
    paginate_by = 15

    def get_queryset(self):
        queryset = super(OpenCourseListView,self).get_queryset()
        course_name = self.request.GET.get('course_name')
        if course_name:
            queryset_by_name = queryset.filter(course__name__contains=course_name)
            return queryset_by_name
        else :
            return queryset

class OpenCourseAdvancedSearchListView(ListView):
    model = OpenCourse
    template_name = "open_course_list.tpl"
    context_object_name = "open_courses"
    paginate_by = 15

    def get_queryset(self):
        queryset = super(OpenCourseAdvancedSearchListView,self).get_queryset()
        data = self.request.GET
        course_name = data.get('course_name')
        course_teacher = data.get('course_teacher')
        course_time = data.get('course_time')
        course_num = data.get('course_num')
        # queryset_by = queryset.filter(Q(course__name__contains=course_name)|Q(course__course_num=course_num)|Q(time__contains=course_time)|Q(teacher__name=course_teacher))
        queryset_by = queryset
        if course_name:
            queryset_by = queryset_by.filter(course__name__contains=course_name)
        if course_teacher:
            queryset_by = queryset_by.filter(teacher__name=course_teacher)
        if course_num:
            queryset_by = queryset_by.filter(course__course_num=course_num)
        if course_time:
            queryset_by = queryset_by.filter(time__contains=course_time)
        return queryset_by

class CourseListView(ListView):
    model = Course
    template_name = "course_list.tpl"
    context_object_name = "courses"
    paginate_by = 15
