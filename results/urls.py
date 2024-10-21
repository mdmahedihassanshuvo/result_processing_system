from django.urls import path
from .views import (
    StudentCreateView,
    StudentListView,
    StudentDetailsView,
    StudentUpdateView
)

app_name = "students"

urlpatterns = [
    # Student URLs
    path('', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path(
        '<int:pk>/details/', StudentDetailsView.as_view(),
        name='student_details'
    ),
    path(
        '<int:pk>/update/', StudentUpdateView.as_view(), name="student_update"
    )
]
