# IMPORT FROM REST FRAMEWORK
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)

# IMPORT FROM DJANGO
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
)

# IMPORT FROM LOCAL
from .models import (
    Student,
    Subject,
    Exam,
    Result,
    ResultPublish
)
from .serializer import (
    StudentSerializer,
    SubjectSerializer,
    ExamSerializer,
    ResultSerializer,
    ResultPublishSerializer
)
from results.forms.student_form import StudentForm

#  Student CRUD view


class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"

    def get_queryset(self):
        return Student.objects.all()


class StudentCreateView(CreateView):
    model = Student
    template_name = "students/student_form.html"
    form_class = StudentForm
    success_url = reverse_lazy("students:student-list")
