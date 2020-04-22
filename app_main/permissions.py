from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin


class IsOwnerMixin(LoginRequiredMixin, SingleObjectMixin):

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
