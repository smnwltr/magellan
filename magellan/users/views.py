from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.forms import modelformset_factory
from django.contrib import messages
from .models import CustomUser, ProfileImage
from .forms import CustomUserUpdateForm, ProfileImageForm


@staff_member_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_profile(request, url_short):
    user = get_object_or_404(CustomUser, url_short=url_short)
    return render(request, 'user_profile.html', {'url_short': url_short, 'user': user})


@login_required
def user_update(request, url_short):
    if request.user.is_staff:
        user = get_object_or_404(CustomUser, url_short=url_short)
    else:
        user = request.user

    profile_image_formset = modelformset_factory(ProfileImage, form=ProfileImageForm, extra=1)

    if request.method == 'POST':

        user_update_form = CustomUserUpdateForm(request.POST, instance=user)

        formset = profile_image_formset(request.POST, request.FILES, queryset=ProfileImage.objects.none())

        if user_update_form.is_valid() and formset.is_valid():
            user_update_form = user_update_form.save(commit=False)
            user_update_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['profile_image']
                    photo = ProfileImage(user=user, image=image)
                    photo.save()
                messages.success(request, 'Profile image upload done')

            return redirect('user_profile', url_short)
        else:
            print(user_update_form.errors)

    else:
        user_update_form = CustomUserUpdateForm(instance=user)
        formset = profile_image_formset(queryset=ProfileImage.objects.none())

    return render(request, 'user_update.html', {'form': user_update_form, 'user': user, 'formset': formset})
