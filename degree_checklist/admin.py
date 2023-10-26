from django.contrib import admin
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment

# Register your models here.
admin.site.register(Student)
admin.site.register(DegreeProgram)
admin.site.register(Course)
admin.site.register(DegreeChecklistTemplate)
admin.site.register(StudentDegreeChecklist)
admin.site.register(CourseEnrollment)
