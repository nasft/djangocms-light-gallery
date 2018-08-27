import re

from django.core.exceptions import ValidationError


def validate_hex(value):
    pattern = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
    if not re.search(pattern, value):
        raise ValidationError(
            '%s is not a valid hex color code of the form #a0b1c2.' % value,
            params={'value': value},
        )
