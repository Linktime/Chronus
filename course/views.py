from django.shortcuts import render
from django.views.generic.list import ListView, MultipleObjectMixin

from course.models import OpenCourse, Course

# Create your views here.

# class MixinByCourseName(MultipleObjectMixin):
#     def get_queryset(self):
#         queryset = super(MixinByCourseName, self).get_queryset()
#         course_name = self.reguest.GET.get('course_name')
#         import code;code.interact(local=locals())
#         if course_name:
#             queryset_name = queryset.filter(course__name=course_name)
#             return queryset_name
#         else :
#             return queryset

class OpenCourseListView(ListView):
    model = OpenCourse
    template_name = "open_course_list.tpl"
    context_object_name = "open_courses"

    def get_queryset(self):
        queryset = super(OpenCourseListView,self).get_queryset()
        course_name = self.request.GET.get('course_name')
        if course_name:
            queryset_by_semester = queryset.filter(course__name__contains=course_name)
            return queryset_by_semester
        else :
            return queryset

class CourseListView(ListView):
    model = Course
    template_name = "course_list.tpl"
    context_object_name = "courses"
