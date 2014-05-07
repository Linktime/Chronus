from django.shortcuts import render
from django.views.generic.list import ListView

from course.models import OpenCourse, Course

# Create your views here.

class OpenCourseListView(ListView):
    model = OpenCourse
    template_name = "open_course_list.tpl"
    context_object_name = "open_courses"

    def get_queryset(self):
        queryset = super(OpenCourseListView,self).get_queryset()
        queryset_by_semester = queryset.filter() # TODO
        return queryset_by_semester

class CourseListView(ListView):
    model = Course
    template_name = "course_list.tpl"
    context_object_name = "courses"
