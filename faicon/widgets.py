from django.forms import Widget
from django.conf import settings
from django.utils.html import format_html
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


FAICON_PREFIX = getattr(settings, 'FAICON_PREFIX', 'fa')
FA_CSS = getattr(settings, 'FAICON_CSS_URL', 'fontawesome/css/all.css')


class Icon:
    """ A Font Awesome Icon object """

    def __init__(self, style=None, icon=None, prefix=FAICON_PREFIX):
        self.style = style
        self.icon = icon
        if prefix:
            self.prefix = '{0}-'.format(prefix)
        else:
            self.prefix = ''

    def icon_html(self, extra=''):
        self.extra = extra

        return format_html(
            '<i class="{style} {prefix}{icon} {extra}"></i>'.format(
                **self.__dict__))

    def __str__(self):
        return 'style:{style},icon:{icon}'.format(**self.__dict__)


def parse_icon(icon_string):
    sep = ','
    kwargs = {}
    if sep in icon_string:
        icon_parts = icon_string.split(sep)
        for i in icon_parts:
            if ':' in i:
                i_args = i.split(':')
                kwargs[i_args[0]] = i_args[1]

        if 'style' not in kwargs or 'icon' not in kwargs:
            raise ValidationError(_("Invalid input for Icon"))
        return Icon(**kwargs)
    else:
        raise ValidationError(_("Invalid input for Icon"))


class IconWidget(Widget):
    template_name = 'faicon/widgets/icon.html'

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget as an HTML string."""
        context = self.get_context(name, value, attrs)

        if value:
            if type(value) == str:
                value = parse_icon(value)
            context['icon_html'] = value.icon_html('fa-3x')

        return self._render(self.template_name, context, renderer)

    class Media:
        css = {
            'all': (
                'faicon/css/faicon.css',
                FA_CSS,
            ),
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.min.js',
            'faicon/js/list.min.js',
            'faicon/js/faicon.js',
        )

