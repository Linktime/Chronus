__author__ = 'hz'
#coding=utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbproject.settings")
from course.models import ChronusUser, Department, StudentInfo, Semester, TeacherRank
from course.models import TeacherInfo, Course, OpenCourse, ElectedCourse
from datetime import datetime
f = open("e://test.csv","r")
tid = 10000000

TODAY = datetime.today()


for line in f.readlines():



        r_list = line.split(",")


        try:

            dep = Department.objects.get(department_num='001')
            sem = Semester.objects.get(begin_year='2011')
            teacher = TeacherInfo.objects.get(user__name=r_list[4])

        except TeacherInfo.DoesNotExist:

            user = ChronusUser(username=str(tid), birth_date=TODAY.date(), name=r_list[4])
            trank2 = TeacherRank.objects.create(name='讲师')
            teacher = TeacherInfo.objects.create(user=user, rank=trank2, salary=9999, department=dep)

            tid+=1

        try:
            course = Course.objects.get(name=r_list[0])

        except Course.DoesNotExist:

            cour = Course.objects.create(course_num=r_list[2], name=r_list[0], credit=float(r_list[1]), period=10,
                              department=dep, course_intro='good course', course_detail='very good course')


            opcour = OpenCourse.objects.create(semester=sem, course=cour,
                                    time=r_list[5]
                                    , capacity=150, information='......', place="J202")