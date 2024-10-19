# IMPORT FROM REST FRAMWORK
from rest_framework import serializers
# IMPORT FROM DJANGO

# IMPROT FROM LOCAL
from .models import (
    Student,
    Subject,
    Exam,
    Result,
    ResultPublish
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class ResultPublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultPublish
        fields = "__all__"
