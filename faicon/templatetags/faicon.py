from django import template
from django.conf import settings

from faicon.models import ICON_LIST, FA_VERSION

register = template.Library()

FAICON_PREFIX = getattr(settings, 'FAICON_PREFIX', 'fa')


@register.inclusion_tag('faicon/icon_list.html', takes_context=True)
def faicon_modal(context, icon_list, fa_version):
    """ just render icon picker once even if multiple widgets """
    return {'icon_list': ICON_LIST, 'fa_version': FA_VERSION}


ICON_STYLES = {
    'solid': 'fas',
    'regular': 'far',
    'light': 'fal',
    'brands': 'fab',
}


@register.inclusion_tag('faicon/icon.html')
def faicon_admin_icon(key, style, label, terms, extra=None):
    if FAICON_PREFIX:
        icon = '{0}-{1}'.format(FAICON_PREFIX, key)
    else:
        icon = key

    try:
        terms_str = ', '.join(terms)
    except:
        terms_str = ''

    return {
        'style': style,
        'style_code': ICON_STYLES[style],
        'icon': icon,
        'label': label,
        'terms': terms_str,
        'extra': extra,
        'key': key,
    }
