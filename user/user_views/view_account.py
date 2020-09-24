from django.shortcuts import render, get_object_or_404
from django.views import View
from user.models import User
from user.decorators import match_username
from django.utils.decorators import method_decorator


class AccountObjectMixin(object):
    model = User
    username = 'username'

    def get_object(self, request):

        obj = None
        if request.user is not None:
            obj = get_object_or_404(self.model, username=request.user.username)

        return obj


class ViewAccount(AccountObjectMixin, View):
    view_template = 'user/user.html'

    @method_decorator(match_username)
    def get(self, request, *args, **kwargs):
        # print(request.user.username)
        # print(request.user.first_name)
        # user_detail = User.objects.filter(username=request.user.username)
        user_detail = self.get_object(request)
        return render(request, self.view_template, {'users': user_detail})

