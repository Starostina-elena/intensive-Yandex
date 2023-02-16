class PositiveNumber:
    regex = '([0-9]+)'

    def to_python(self, value):
        if int(value) > 0:
            return int(value)
        raise ValueError

    def to_url(self, value):
        return str(value)
