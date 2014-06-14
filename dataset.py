#coding=utf-8
import os
from datetime import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbproject.settings")
from course.models import SiteSettings
from course.models import ChronusUser, Department, StudentInfo, Semester, TeacherRank
from course.models import TeacherInfo, Course, OpenCourse, ElectedCourse

sem1 = Semester.objects.create(begin_year=2011, season='S')
sem2 = Semester.objects.create(begin_year=2011, season='W')

ss = SiteSettings(current_semester=sem1)
ss.save()

Dep1 = Department.objects.create(department_num='005', name='计算机学院',address='东区',
                                 phone='404')
Dep2 = Department.objects.create(department_num='006', name='通信学院', address='东区计院旁',
                                 phone='500')

TODAY = datetime.today()

su1 = ChronusUser(username='11121281',birth_date=TODAY.date())
su1.set_password('123456')
su1.save()

su2 = ChronusUser(username='11121282', birth_date=TODAY.date())
su2.set_password('123456')
su2.save()

stu1 = StudentInfo.objects.create(user=su1, province='北京',phone='12134123',
                                  entrance_semester=sem1, department=Dep1)
stu2 = StudentInfo.objects.create(user=su2, province='上海', phone='1231313',
                                  entrance_semester=sem2, department=Dep2)

'''
tu1 = ChronusUser(username='10005678', birth_date=TODAY.date(),name=u"宋安平")
tu1.set_password('123456')
tu1.save()
tu2 = ChronusUser(username='10001234', birth_date=TODAY.date(),name=u"李卫民")
tu2.set_password('123456')
tu2.save()








trank1 = TeacherRank.objects.create(name='教授')
trank2 = TeacherRank.objects.create(name='讲师')



teacher1 = TeacherInfo.objects.create(user=tu1, rank=trank1, salary=19999, department=Dep1)
teacher2 = TeacherInfo.objects.create(user=tu2, rank=trank2, salary=9999, department=Dep2)

cour1 = Course.objects.create(course_num='0001', name='并行计算', credit=4, period=10,
                              department=Dep1,
                              course_intro='good course', course_detail='very godd course')

cour2 = Course.objects.create(course_num='0002', name='汇编语言', credit=4, period=10,
                              department=Dep1,
                              course_intro='good course', course_detail='very godd course')

opcour1 = OpenCourse.objects.create(semester=sem1, course=cour1,
                                    time='一1-3,三7-8'
                                    , capacity=150, information='......', place="J202")

opcour2 = OpenCourse.objects.create(semester=sem2, course=cour2,
                                    time='一1-3,三7-8'
                                    , capacity=150, information='......', place="J101")
opcour1.teacher.add(tu1,tu2)
opcour2.teacher.add(tu1)

ecour1 = ElectedCourse.objects.create(student=su1, course=opcour1,
                                      usual_score=80, exam_score=85, score=0.3*80 + 0.7*85)

ecour2 = ElectedCourse.objects.create(student=su1, course=opcour2,
                                      usual_score=70, exam_score=85)

ecour2 = ElectedCourse.objects.create(student=su2, course=opcour2,
                                      usual_score=80, exam_score=85)
'''
