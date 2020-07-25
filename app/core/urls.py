from django.conf.urls import url
from django.urls import path
from app.core.views import MainPageView, LoginView, ProfilePage, RegisterView


urlpatterns = [
    url(r'^accounts/register/$', RegisterView.as_view(), name="register"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    path('', MainPageView.as_view()),
]
