from dataclasses import field
from rest_framework import serializers
from .models import Student

class StudentSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


