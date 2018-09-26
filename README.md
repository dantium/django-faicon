# django-faicon
Integrates a Font Awesome 5 icon picker in the Django admin interface. Picker interface includes dynamic search on the icon name & terms, filter by styles and can handle thousands of icons easily. Package uses the free version of Font Awesome but you can easily drop in the Pro version if you have license.

![Admin Preview GIF](https://github.com/dantium/django-faicon/raw/master/admin_preview.gif "Admin Preview")

## Documentation 

### Install

```python
pip install django-faicon
```
Add `faicon` to `INSTALLED_APPS` in `settings`

Add `path('faicon/', include('faicon.urls')),` to `urlpatterns` in `urls.py`

Add the field to your model

```python
from faicon.fields import FAIconField

class MyModel(models.Model):
    icon = FAIconField()
```

### Setup

If you want to use Font Awesome Pro or a different version than the one included, download it and put it in your project static directory and name it `fontawesome`

To specify different locations for the icon files you can use these settings:

```python
FAICON_YAML_FILE = 'fontawesome/metadata/icons.yml'
FAICON_CSS_URL = 'fontawesome/css/all.css'
```

