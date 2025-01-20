import ulid
from django.db import models


class ULIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 26
        kwargs['default'] = ulid.new
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)
