from django import forms

# IMPORT FROM LOCAL
from results.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "roll_number",
            "name",
            "class_level",
            "date_of_birth"
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={
                'type': 'date',
                'class': 'datepicker',
                'placeholder': 'Select date'
                }),
        }
