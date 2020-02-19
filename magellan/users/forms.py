from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, ProfileImage


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(), max_length=50, label='First name', )
    last_name = forms.CharField(widget=forms.TextInput(), max_length=50, label='Last name', required=False)
    handle = forms.CharField(widget=forms.TextInput(), max_length=20, label='Nickname', required=False)
    home_town = forms.CharField(widget=forms.TextInput(), max_length=50, label='City', required=False)
    home_country = forms.CharField(widget=forms.TextInput(), max_length=50, label='Country', required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'home_town', 'home_country', 'handle')

    # TODO: Let staff members change owner and active booleans
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
    #     if not user.is_staff:
    #         del self.fields['is_owner']


class ProfileImageForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Change profile image')

    class Meta:
        model = ProfileImage
        fields = ['profile_image', ]
