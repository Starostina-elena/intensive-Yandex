import re

from django.core import exceptions


def validator_word_good(value):
    words = set(re.compile(r'\w+|\W+').findall(value.lower()))
    if 'превосходно' not in words and 'роскошно' not in words:
        raise exceptions.ValidationError('В тексте должно быть '
                                         'слово "превосходно" или "роскошно"')
