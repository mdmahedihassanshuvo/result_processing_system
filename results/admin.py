from django.contrib import admin

# IMPORT FROM LOCAL
from .models import (
    Student
)

admin.site.register(Student)
