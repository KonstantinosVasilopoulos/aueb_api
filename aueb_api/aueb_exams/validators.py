from django.core.validators import RegexValidator

# DD/MM/YYYY date format validator
exam_date_validator = RegexValidator(
    regex=r'^([0-9][1-9]\/){2}[0-9]{4}$',
    message='Date must be of "DD/MM/YYYY" format.',
    code='invalid_date_format'
)

# HH:MM-HH:MM time format validator
exam_time_validator = RegexValidator(
    regex=r'^[0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2}$',
    message='Time must be of "HH:MM-HH:MM" format.',
    code='invalid_time_format'
)
