from django.db import models
from aueb_exams.validators import exam_date_validator,exam_time_validator


class Exam(models.Model):
    """ Class representing a single examination date. """
    id = models.AutoField(primary_key=True, verbose_name='id', db_column='ex_id')
    date = models.CharField(verbose_name='date', max_length=10, db_column='ex_date', validators=[exam_date_validator])
    time = models.CharField(verbose_name='time', max_length=11, db_column='ex_time', validators=[exam_time_validator])
    room = models.CharField(verbose_name='room', max_length=255, db_column='ex_room')
    department = models.CharField(verbose_name='department', max_length=255, db_column='ex_department')
    professor = models.CharField(verbose_name='professor', max_length=255, db_column='ex_professor', blank=True, null=True)
    course = models.CharField(verbose_name='course', max_length=255, db_column='ex_course')
    notes = models.TextField(verbose_name='notes', db_column='ex_notes')


    def __str__(self) -> str:
        return 'Exam(id: {}, date: {}, time: {}, room: {}, department: {}, professor: {}, course: {}, notes: {})'.format(
            self.id,
            self.date,
            self.time,
            self.room,
            self.department,
            self.professor,
            self.course,
            self.notes
        )


    class Meta:
        db_table = 'exams'
