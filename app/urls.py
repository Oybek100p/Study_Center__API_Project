from django.urls import path
from .views import classroom_list, createClassroom, update_class, classroom_delete, student_delete, student_list, update_student, createStudent

urlpatterns = [
    # Class
    path('classroom-list/', classroom_list, name='classroom_list'),
    path('create-classroom/', createClassroom, name='create-classroom'),
    path('classroom-update/<int:pk>/', update_class, name='create-update'),
    path('classroom-delete/<int:pk>/', classroom_delete, name='create-delete'),
    # Student
    path('student-list/', student_list, name='student_list'),
    path('create-student/', createStudent, name='create-student'),
    path('student-update/<int:pk>/', update_student, name='student-update'),
    path('student-delete/<int:pk>/', student_delete, name='student-delete'),
]