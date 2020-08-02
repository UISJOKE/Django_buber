from django.urls import path
from app.core.views import MyRegisterFormView, MainPageView, profile, LoginView, LogoutView

urlpatterns = [
    path('signup/', MyRegisterFormView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name="profile"),
    path('', MainPageView.as_view(), name='home'),
]
