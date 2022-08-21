from dataclasses import field
from aueb_exams.models import Exam
from rest_framework import serializers


class ExamSerializer(serializers.ModelSerializer):
    """ Serializer for the exam class. """
    class Meta:
        model = Exam
        fields = '__all__'
