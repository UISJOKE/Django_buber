from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms
from django.contrib.auth import get_user_model

from app.core import models


class SignUpForm(UserCreationForm):
    GENDER_CHOICES = (('Male', 'Male'),
                      ('Female', 'Female'))
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    male = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'male', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = models.User
        fields = ['username', 'email', 'bio', 'car', 'male', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['avatar']
