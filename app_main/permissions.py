from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.detail import SingleObjectMixin


class IsOwnerMixin(TemplateResponseMixin, LoginRequiredMixin, SingleObjectMixin):
    success_template_name = None
    failed_template_name = None

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        self.template_name = self.success_template_name or self.template_name
        if instance.author != request.user:
            if self.failed_template_name is None:
                return self.handle_no_permission()
            self.template_name = self.failed_template_name
        return super().dispatch(request, *args, **kwargs)
