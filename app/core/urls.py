from django.conf.urls import url
from django.urls import path
from app.core.views import MyRegisterFormView, MainPageView, ProfilePage, LoginView

urlpatterns = [
    path('signup/', MyRegisterFormView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfilePage.as_view(), name="profile"),
    path('', MainPageView.as_view(), name='home'),
]
