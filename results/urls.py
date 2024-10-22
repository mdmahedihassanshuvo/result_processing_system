from django.urls import path
from .views import (
    StudentCreateView,
    StudentListView,
    StudentDetailsView,
    StudentUpdateView,
    SubjectListView
)

urlpatterns = [
    # Student URLs
    path('v1/students/', StudentListView.as_view(), name='student-list'),
    path(
        'v1/students/create/', StudentCreateView.as_view(),
        name='student_create'
    ),
    path(
        'v1/students/<int:pk>/details/', StudentDetailsView.as_view(),
        name='student_details'
    ),
    path(
        'v1/students/<int:pk>/update/', StudentUpdateView.as_view(),
        name="student_update"
    ),

    path(
        'v1/subjects/', SubjectListView.as_view(), name='subject_list'
    )
]
