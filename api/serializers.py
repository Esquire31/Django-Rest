from dataclasses import field
from statistics import mode
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    # Allows Concerting Complex Data into Native Python datatypes
    class Meta:
        model = Course
        fields = '__all__'
