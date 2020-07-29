from django.contrib.auth import login, authenticate, logout, get_user_model
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm
from django.views.generic import TemplateView, FormView, RedirectView


class MainPageView(TemplateView):
    template_name = 'core/main_page.html'


class MyRegisterFormView(FormView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = "core/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "core/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if get_user_model():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class ProfilePage(TemplateView):
    template_name = "core/profile.html"
