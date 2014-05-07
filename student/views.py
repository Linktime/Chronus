from django.shortcuts import render
from django.views.generic.list import ListView, MultipleObjectMixin
from django.http import Http404
from course.models import ElectedCourse
from django.contrib.auth.views import get_user_model
# Create your views here.

class MixinByStudent(MultipleObjectMixin):
    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous():
            raise Http404()
        queryset = super(MixinByStudent, self).get_queryset()
        queryset_by_student = queryset.filter(student=self.request.user)
        return queryset_by_student

class ElectedCourseListView(ListView,MixinByStudent):
    model = ElectedCourse
    template_name = 'student/elected_course_list.tpl'
    context_object_name = 'elected_course_list'