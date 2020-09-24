from django.shortcuts import render, redirect
from django.views import View
from user.forms import RegisterForm, ProfileForm
from django.contrib import messages


class CreateAccount(View):
    user_form = RegisterForm
    profile_form = ProfileForm
    form_template = 'user/register.html'

    def get(self, request, *args, **kwargs):
        user_form = self.user_form
        profile_form = self.profile_form
        return render(request, self.form_template, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user_form = self.user_form(request.POST)
        profile_form = self.profile_form(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            email = user_form.cleaned_data.get('email')
            messages.success(request, f'Your account {email} has been created! Use your credential to login!')
            return redirect('user:login')

        return render(request, self.form_template, {'user_form': user_form, 'profile_form': profile_form})










