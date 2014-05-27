# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list import ListView, MultipleObjectMixin
from django.contrib.auth import logout
from course.models import ElectedCourse, OpenCourse
from django.contrib import messages
import re

from course.models import OpenCourse, Course, SiteSettings

ss = SiteSettings.objects.filter()
current_semester = ss[0].current_semester

def index(request):
    print request.user
    if request.user.is_authenticated():
        print request.user.is_teacher()
    return render_to_response('index.tpl',context_instance=RequestContext(request))

def course_profile(request, ocid):
    try:
        ocourse = OpenCourse.objects.get(id=int(ocid))
    except ObjectDoesNotExist:
        ocourse = None
    return render_to_response('course_profile.tpl', {"ocourse": ocourse}, context_instance=RequestContext(request))


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
        queryset = queryset.filter(semester=current_semester)
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
        queryset = queryset.filter(semester=current_semester)
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
            queryset_by = queryset_by.filter(teacher__name__contains=course_teacher)
        if course_num:
            queryset_by = queryset_by.filter(course__course_num__contains=course_num)
        if course_time:
            queryset_by = queryset_by.filter(time__contains=course_time)
        return queryset_by

    def get_context_data(self, **kwargs):
        context = super(OpenCourseAdvancedSearchListView,self).get_context_data(**kwargs)
        data = self.request.GET
        search_arg = "&course_name=%s&course_teacher=%s&course_time=%s&course_num=%s" %\
                     (data.get("course_name"),data.get("course_teacher"),data.get("course_time"),data.get("course_num"))
        context["search_arg"] = search_arg
        return context

class CourseListView(ListView):
    model = Course
    template_name = "teacher/course_list.tpl"
    context_object_name = "courses"
    paginate_by = 15

def elected_course(request,user,course_list):
    for course_id in course_list:
            course = OpenCourse.objects.get(id=course_id,semester=current_semester)
            if course.elected_count()==course.capacity:
                messages.warning(request,u"课程《%s》选取失败，已超人数限制！"%course.course.name)
            else:
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

def cancel_elected(request,user,course_list):
    for course_id in course_list:
            course = OpenCourse.objects.get(id=course_id,semester=current_semester)
            try :
                elected_course = ElectedCourse.objects.get(student=user,course=course)
                elected_course.delete()
                messages.success(request,u"课程《%s》退课成功，你可以继续选择其它课程或者退课！"%course.course.name)
            except ElectedCourse.DoesNotExist :
                messages.warning(request,u"课程《%s》还未选取！"%course.course.name)