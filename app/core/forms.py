from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not get_user_model().is_active:
            raise forms.ValidationError(
                'Этот аккаунт не активен!'
            )
