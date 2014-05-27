from django.contrib import admin
from models import *

admin.site.register(ChronusUser)
admin.site.register(Department)
admin.site.register(TeacherRank)

admin.site.register(Course)
admin.site.register(ElectedCourse)
admin.site.register(OpenCourse)

admin.site.register(Semester)
