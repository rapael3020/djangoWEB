from profileapp.models import profile
from django.http import HttpResponseForbidden


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        Profile = profile.objects.get(pk=kwargs['pk'])
        if not Profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated