from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    MyLogoutView,
    AboutMeView,
    RegisterView,
    BalanceUpdateView,
)


app_name = 'app_users'

urlpatterns = [
    #path('login/', login_view, name='login')
    path(
        'login/',
        LoginView.as_view(
            template_name='app_users/login.html',
            redirect_authenticated_user=True,
        ),
        name='login'),

    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('register/', RegisterView.as_view(), name='register'),
    path('add-balance/', BalanceUpdateView.as_view(), name='add-balance'),
]
