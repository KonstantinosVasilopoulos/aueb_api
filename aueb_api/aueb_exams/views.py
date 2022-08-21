from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from aueb_exams.models import Exam
from aueb_exams.serializers import ExamSerializer


class ExamViewSet(viewsets.ReadOnlyModelViewSet):
    """ View for serving serialized exam objects. """
    queryset = Exam.objects.all().order_by('id')
    serializer_class = ExamSerializer


    def filter_queryset(self, queryset):
        """ Filter the queryset using the query parameters provided in the URL. """
        # Date query parameter
        if 'date' in self.request.GET:
            # Format the date
            date = self.request.GET.get('date', None)
            if len(date) == 8:
                date = '{}/{}/{}'.format(date[:2], date[2:4], date[4:8])
            else:  # Return 400 Bad Request error
                raise ValidationError('Bad date format: {}'.format(date), code=400)

            queryset = queryset.filter(date=date)

        # Department query parameter
        if 'department' in self.request.GET:
            department = self.request.GET.get('department', None)
            queryset = queryset.filter(department__contains=department)

        # Professor query parameter
        if 'professor' in self.request.GET:
            professor = self.request.GET.get('professor', None)
            queryset = queryset.filter(professor__contains=professor)

        # Course query parameter
        if 'course' in self.request.GET:
            course = self.request.GET.get('course', None)
            queryset = queryset.filter(course=course)

        return queryset
