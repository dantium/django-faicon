import yaml
import re

from django.conf import settings
from django.contrib.staticfiles.finders import find

YAML_FILE = getattr(
    settings,
    'FAICON_YAML_FILE',
    'fontawesome/metadata/icons.yml'
)
FA_CSS = getattr(settings, 'FAICON_CSS_URL', 'fontawesome/css/all.css')


def get_icon_list():
    file = find(YAML_FILE)
    if not file:
        raise ValueError(
            "Faicon - can't find {}, \
            check FAICON_YAML_FILE setting.".format(YAML_FILE)
        )
    with open(file, 'r') as stream:
        data_loaded = yaml.load(stream)
    return data_loaded


def get_iconset_version():
    version = 'Font Awesome'
    r = re.compile(' \* (.*?) by ')
    if FA_CSS.startswith('http'):
        pass
    else:
        file = find(FA_CSS)
        if file:
            with open(file, 'r') as stream:
                version = stream.readlines()[1]
                m = r.search(version)
                if m:
                    version = m.group(1)
    return version


ICON_LIST = get_icon_list()
FA_VERSION = get_iconset_version()
