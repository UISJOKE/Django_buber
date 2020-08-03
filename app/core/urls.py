from django.urls import path
from app.core.views import MyRegisterFormView, MainPageView, profile, LoginView, LogoutView, number_model, car

urlpatterns = [
    path('signup/', MyRegisterFormView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name="profile"),
    path('add/number&model/', number_model, name='add_model_number'),
    path('add/car/', car, name='add_car'),
    path('', MainPageView.as_view(), name='home'),
]
