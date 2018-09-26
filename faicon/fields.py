from django.db import models
from django.utils.translation import gettext_lazy as _

from .widgets import IconWidget, Icon, parse_icon


ICON_STYLES = (
    ('fas', 'solid'),
    ('far', 'regular'),
    ('fal', 'light'),
    ('fab', 'brands'),
)


class FAIconField(models.Field):
    description = _('Font Awesome 5 Icon Field')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def from_db_value(self, value, expression, connection):
        if isinstance(value, Icon):
            return value
        if not value:
            return value
        return parse_icon(value)

    def to_python(self, value):
        if isinstance(value, Icon):
            return value
        if not value:
            return value
        return parse_icon(value)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if isinstance(value, str) or value is None:
            return value
        return str(value)

    def formfield(self, **kwargs):
        defaults = {'widget': IconWidget}
        defaults.update(kwargs)
        return super().formfield(**defaults)
