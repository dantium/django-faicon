from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        'render_icon_list_modal/',
        TemplateView.as_view(
            template_name='faicon_modal.html'
        ),
        name='faicon-modal'
    ),
]
