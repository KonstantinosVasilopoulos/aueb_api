from django.core.validators import RegexValidator

# DDMMYYYY date format validator
exam_date_validator = RegexValidator(
    regex=r'^([0-9][1-9]){2}[0-9]{4}$',
    message='Date must be of "DDMMYY" format.',
    code='invalid_date_format'
)

# TODO: HH:MM-HH:MM time format validator
exam_time_validator = None
