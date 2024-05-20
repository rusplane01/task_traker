from django.core.exceptions import PermissionDenied

class UserisOwnerMixin():
    def dispatch(self, *args, **kwargs):
        instance = self.get_object()
        if instance.creator != self.request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request, *args, **kwargs)
