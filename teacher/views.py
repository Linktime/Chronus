#coding=utf-8
from django.http import HttpResponseRedirect
from django.forms import Form
import django.forms
from django.forms.formsets import formset_factory
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from course.models import OpenCourse, ElectedCourse, SiteSettings, Semester, ChronusUser
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
# Create your views here.
class GradeForm(Form):
    eid = django.forms.IntegerField(min_value=0, widget=django.forms.HiddenInput())
    snum = django.forms.CharField(label="学号", widget=django.forms.TextInput(attrs={"readonly": "true"}))
    sname = django.forms.CharField(label="学生姓名", widget=django.forms.TextInput(attrs={"readonly": "true"}))
    usualgrade = django.forms.IntegerField(label="平时成绩", min_value=0, max_value=100)
    finalgrade = django.forms.IntegerField(label="考试成绩", min_value=0, max_value=100)
    score = django.forms.IntegerField(widget=django.forms.TextInput(attrs={"readonly": "true"}))

class RatioForm(Form):
    exam_ratio = django.forms.FloatField(min_value=0.0, max_value=1.0, label=u"期末考分占比")

GradeFormSet = formset_factory(GradeForm, extra=0)

def teacher_required(func):
    def rfunc(request, *args, **kargs):
        if request.user.is_authenticated() and not request.user.is_teacher():
            return HttpResponseRedirect("/")
        else:
            return func(request, *args, **kargs)
    return rfunc

@login_required
@teacher_required
def uploadgrade(request, ocourseid):
    if request.method == "GET":
        ocourseid = int(ocourseid)
        try:
            ocourse = OpenCourse.objects.get(id=ocourseid)
        except ObjectDoesNotExist:
            return HttpResponseRedirect("/")
        electedcourses = ElectedCourse.objects.filter(course=ocourse)
        initialdata = []
        for elecourse in electedcourses:
            initialdata.append({"snum": elecourse.student.username,
                                "sname": elecourse.student.name,
                                "eid": elecourse.id,
                                "usualgrade": elecourse.usual_score,
                                "finalgrade": elecourse.exam_score,
                                "score": elecourse.score})
        print initialdata
        formset = GradeFormSet(initial=initialdata)
        return render_to_response("teacher/uploadgrade.tpl", {"formset": formset, "ocourse": ocourse,
                                                              "ratioform": RatioForm({"exam_ratio": 0.7})},
                                  context_instance=RequestContext(request))
    elif request.method == "POST":
        ocid = int(ocourseid)
        try:
            ocourse = OpenCourse.objects.get(id=ocid)
        except ObjectDoesNotExist:
            return HttpResponseRedirect("/")
        if not request.user in ocourse.teacher.all():
            return HttpResponseRedirect("/")
        formset = GradeFormSet(request.POST)
        ratioform = RatioForm(request.POST)
        if not (formset.is_valid() and ratioform.is_valid()):
            return render_to_response("teacher/uploadgrade.tpl", {"formset": formset, "ocourse": ocourse,
                                                                  "ratioform": ratioform},
                                      context_instance=RequestContext(request))
        else:
            #print "::", formset[0].cleaned_data
            for form in formset:
                data = form.cleaned_data
                elecourse = ElectedCourse.objects.get(id=data['eid'])
                elecourse.usual_score = data["usualgrade"]
                elecourse.exam_score = data["finalgrade"]
                exam_score_ratio = ratioform.cleaned_data["exam_ratio"]
                elecourse.score = elecourse.usual_score * (1 - exam_score_ratio) + elecourse.exam_score * exam_score_ratio
                elecourse.save()
                #print data

        return HttpResponseRedirect(".")
    else:
        return HttpResponseRedirect("/")

@login_required
@teacher_required
def current_courselist(request):
    courses = OpenCourse.objects.filter(semester=SiteSettings.objects.all()[0].current_semester).filter(teacher=request.user)
    #courses = ChronusUser.OpenCourses.filter(semester=SiteSettings.objects.all()[0].current_semester)
    #currentsemester = SiteSettings.objects.all()[0].current_semester
    #courses = filter(lambda c: c.semester == currentsemester, ChronusUser.opencourse_set.all())
    return render_to_response("teacher/course_list.tpl", {"courses": courses}, context_instance=RequestContext(request))

@login_required
@teacher_required
def all_courselist(request):
    courses = OpenCourse.objects.filter(teacher=request.user)
    return render_to_response("teacher/course_list.tpl", {"courses": courses}, context_instance=RequestContext(request))