from django.urls import path
from . import views, form_views, record_views, import_views

urlpatterns = [
    # Existing views and forms URLs
    path('all_records/', views.all_records, name='all_records'),
    path('create_student/', form_views.create_student, name='create_student'),
    path('create_degree_program/', form_views.create_degree_program,
         name='create_degree_program'),
    path('create_course/', form_views.create_course, name='create_course'),
    path('create_degree_checklist_template/', form_views.create_degree_checklist_template,
         name='create_degree_checklist_template'),
    path('create_student_degree_checklist/', form_views.create_student_degree_checklist,
         name='create_student_degree_checklist'),
    path('create_course_enrollment/', form_views.create_course_enrollment,
         name='create_course_enrollment'),

    # Record views URLs (Updated with underscores)
    path('student_records/', record_views.StudentAllRecordsView.as_view(),
         name='student_records'),
    path('degree_program_records/', record_views.DegreeProgramAllRecordsView.as_view(),
         name='degree_program_records'),
    path('course_records/', record_views.CourseAllRecordsView.as_view(),
         name='course_records'),
    path('degree_checklist_template_records/', record_views.DegreeChecklistTemplateAllRecordsView.as_view(),
         name='degree_checklist_template_records'),
    path('student_degree_checklist_records/', record_views.StudentDegreeChecklistAllRecordsView.as_view(),
         name='student_degree_checklist_records'),
    path('course_enrollment_records/', record_views.CourseEnrollmentAllRecordsView.as_view(),
         name='course_enrollment_records'),

    # Import view URL
    path('data-import/', import_views.data_import_view, name='data_import_view'),
]
