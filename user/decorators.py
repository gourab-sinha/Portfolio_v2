from functools import wraps
from django.http import HttpResponseRedirect


def match_username(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        username = request.user.username
        if username =='gourabsinha':
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/')

    return wrap
