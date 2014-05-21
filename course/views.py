from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView, MultipleObjectMixin
from django.contrib.auth import logout

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
            queryset_by_semester = queryset.filter(course__name__contains=course_name)
            return queryset_by_semester
        else :
            return queryset

class CourseListView(ListView):
    model = Course
    template_name = "course_list.tpl"
    context_object_name = "courses"
    paginate_by = 15
