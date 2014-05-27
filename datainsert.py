__author__ = 'hz'
#coding=utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbproject.settings")
from course.models import ChronusUser, Department, StudentInfo, Semester, TeacherRank
from course.models import TeacherInfo, Course, OpenCourse, ElectedCourse
from datetime import datetime
f = open("./book_back.csv","r")
tid = 10000000

TODAY = datetime.today()

try:
    dep = Department.objects.get(department_num='001')
except Department.DoesNotExist:
    dep = Department.objects.create(department_num='001', name='计算机学院',address='东区',
                                 phone='404')
try :
    sem = Semester.objects.get(begin_year=2011,season='S')
except Semester.DoesNotExist:
    sem = Semester.objects.create(begin_year=2011, season='S')

for line in f.readlines():
        r_list = line.split(",")
        try:
            cour = Course.objects.get(name=r_list[0])
        except Course.DoesNotExist:
            cour = Course.objects.create(course_num=r_list[2], name=r_list[0], credit=float(r_list[1]), period=10,
                              department=dep, course_intro='good course', course_detail='very good course')

        try :
            r_list[6] = int(r_list[6])
        except:
            r_list[6] = 150

        opcour = OpenCourse.objects.create(semester=sem, course=cour,
                                time=r_list[5]
                                , capacity=r_list[6], information='......', place="J202")

        teachers_str = r_list[4].split(' ')
        for teacher_str in teachers_str:
            t_str = teacher_str.strip()
            if t_str.endswith("等"):
                t_str = t_str[:-1]
            try:
                teacher_user = ChronusUser.objects.get(name=t_str)
                opcour.teacher.add(teacher_user)
            except ChronusUser.DoesNotExist:
                teacher_user = ChronusUser(username=str(tid), birth_date=TODAY.date(), name=t_str)
                teacher_user.set_password("123456")
                teacher_user.save()
                trank2 = TeacherRank.objects.create(name='讲师')
                teacher = TeacherInfo.objects.create(user=teacher_user, rank=trank2, salary=9999, department=dep)
                tid+=1
                opcour.teacher.add(teacher_user)
            except:
                pass