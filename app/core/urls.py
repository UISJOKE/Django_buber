from django.urls import path
from app.core.views import MyRegisterFormView, MainPageView, ProfileUpdateView, LoginView, LogoutView, NumberUpdateView, CarUpdateView, ModelUpdateView

urlpatterns = [
    path('signup/', MyRegisterFormView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name="profile"),
    path('add/car/car_number/<int:pk>/', NumberUpdateView.as_view(), name='add_number'),
    path('add/car/car_model/<int:pk>/', ModelUpdateView.as_view(), name='add_model'),
    path('add/car/<int:pk>', CarUpdateView.as_view(), name='add_car'),
    path('', MainPageView.as_view(), name='home'),
]
