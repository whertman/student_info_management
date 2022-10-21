from django import forms
from .models import Student

class Student_Name(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "last_name",
            "first_name",
            "major",
            "email",
        ]

