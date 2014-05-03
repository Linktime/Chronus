#!/usr/bin/python
#coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings

#ActiveUser = django.contrib.auth.get_user_model()
ActiveUser = settings.AUTH_USER_MODEL


class ChronusUser(AbstractBaseUser):
    # TODO Write validations to ensure correct username format (eg. 11121111)
    identifier = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=2, choices=((u"M", u"男"), (u"F", u"女")))
    birth_date = models.DateField()
    department = models.ForeignKey("Department")  # 院系
    available = models.BooleanField(default=True)
    USERNAME_FIELD = "identifier"
    REQUIRED_FIELDS = ["xm", "xb"]


class Department(models.Model):
    department_num = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)


class StudentInfo(models.Model):
    user = models.OneToOneField(ActiveUser, primary_key=True)
    province = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    entrance_semester = models.ForeignKey("Semester")


class FlunkoutWarning(models.Model):
    student = models.OneToOneField(ActiveUser, primary_key=True)
    semester = models.ForeignKey("Semester")


class TeacherRank(models.Model):
    RankNames = (
        (u"P", u"教授"),
        (u"AP", u"副教授"),
        (u"L", u"讲师"),
    )
    name = models.CharField(max_length=2, choices=RankNames)


class TeacherInfo(models.Model):
    user = models.OneToOneField(ActiveUser, primary_key=True)
    rank = models.ForeignKey(TeacherRank)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = models.ForeignKey(Department)


class Course(models.Model):
    course_num = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    credit = models.IntegerField()
    period = models.IntegerField()
    department = models.ForeignKey(Department)
    course_intro = models.CharField(max_length=300)
    course_detail = models.TextField(max_length=2000)


class OpenCourse(models.Model):
    semester = models.ForeignKey("Semester")
    course = models.ForeignKey(Course)
    teacher = models.ManyToManyField(ActiveUser)  # one course can have multiple teachers
    time = models.CharField(max_length=30)
    capacity = models.IntegerField()  # 容量 --- 新增字段
    information = models.TextField(max_length=2000)


class ElectedCourse(models.Model):
    student = models.ForeignKey(ActiveUser)
    course = models.ForeignKey(OpenCourse)
    usual_score = models.IntegerField(null=True)
    exam_score = models.IntegerField(null=True)
    score = models.IntegerField(null=True)


class Semester(models.Model):
    begin_year = models.IntegerField()
    SEASONS = (
        (u"S", u"春季"),
        (u"X", u"夏季"),
        (u"A", u"秋季"),
        (u"W", u"冬季"),
    )
    season = models.CharField(max_length=1, choices=SEASONS)

    @property
    def semester(self):
        return u"%s-%d %s" % (self.begin_year, int(self.begin_year)+1, self.get_season_display())

    class Meta:
        unique_together = ("begin_year", "season")