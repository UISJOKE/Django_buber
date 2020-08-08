from django.contrib.auth import login, authenticate, logout, get_user_model
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm, LoginForm, UserUpdateForm, AddCarForm, AddCarNumberForm, AddCarModelForm
from django.views.generic import TemplateView, FormView, RedirectView, UpdateView,CreateView
from .models import User, CarNumber, Model, Car


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

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.id})


class LogoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if get_user_model():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'core/profile.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.id})


class NumberUpdateView(CreateView):
    model = CarNumber
    form_class = AddCarNumberForm
    template_name = 'core/add_number.html'

    def get_success_url(self):
        return reverse('add_car', kwargs={'pk': self.request.user.id})


class ModelUpdateView(CreateView):
    model = Model
    form_class = AddCarModelForm
    template_name = 'core/add_model.html'

    def get_success_url(self):
        return reverse('add_car', kwargs={'pk': self.request.user.id})


class CarUpdateView(CreateView):
    model = Car
    form_class = AddCarForm
    template_name = 'core/add_car.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.id})

