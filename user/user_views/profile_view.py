from django.views import View
from user.forms import ProfileImageForm
from django.shortcuts import render, redirect


class ProfileView(View):
    profile_template = 'user/profile_image.html'
    profile_image_form = ProfileImageForm

    def get(self, request, *args, **kwargs):
        profile_image_form = self.profile_image_form
        return render(request, self.profile_template, {'profile_image_form': profile_image_form})

    def post(self, request, *args, **kwargs):
        profile_image_form = self.profile_image_form(request.POST)
        print(request.POST)
        if profile_image_form.is_valid():

            profile_image_form.save()
            return redirect('user:register')

        return render(request, self.profile_template, {'profile_image_form': profile_image_form})

