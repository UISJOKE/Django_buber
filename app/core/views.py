from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm, UserUpdateForm, AddCarForm, AddCarNumberForm, AddCarModelForm
from django.views.generic import TemplateView, FormView, RedirectView, UpdateView
from django.contrib import messages
from .models import User


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




class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'core/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        return get_object_or_404(User, pk=pk)


@login_required
def number_model(request):
    if request.method == 'POST':
        number = AddCarNumberForm(request.POST)
        model = AddCarModelForm(request.POST)

        if number.is_valid() and model.is_valid():
            number.save()
            model.save()
            messages.success(request, f'Number and model of car has been add!')
            return redirect('add_car')

    else:
        number = AddCarNumberForm()
        model = AddCarModelForm()

        context = {
            'number': number,
            'model': model
        }
        return render(request, 'core/add_model_number.html', context)


@login_required
def car(request):
    if request.method == 'POST':
        auto = AddCarForm(request.POST)

        if auto.is_valid():
            auto.save()
            messages.success(request, f'Car has been add!')
            return redirect('profile')

    else:
        auto = AddCarForm()

        context = {
            'car': auto
        }
        return render(request, 'core/add_car.html', context)

# class CarUpdateView(UpdateView):
#     model = Car
#     form_class = AddCarForm
#     template_name = 'core/add_car.html'
#     success_url = reverse('profile')
#
#     def get_object(self, queryset=None):
#         pk = self.kwargs.get(self.pk_url_kwarg, None)
#         return get_object_or_404(UserProfile, pk=pk)
