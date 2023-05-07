from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView

from .forms import BalanceForm
from .models import Profile, Balance
from .models import User
import logging

logger = logging.getLogger(__name__)


class BalanceUpdateView(UserPassesTestMixin, UpdateView):
    model = Balance
    template_name_suffix = '_update_form'
    form_class = BalanceForm
    permission_required = 'app_user.change_profile'

    def get_object(self, queryset=None):
        logger.info('Запрошена страница пополнения баланса')
        return Balance.objects.get(user_id=self.request.user.id)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return self.get_object().user == self.request.user \
                or self.request.user.has_perm(self.permission_required)

    def get_success_url(self):
        return reverse(
            'app_users:about-me'
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class AboutMeView(DetailView):

    template_name = 'app_users/about-me.html'
    model = Profile
    context_object_name = "profile"

    def get_object(self, queryset=None):
        profile = Profile.objects.get(user_id=self.request.user.id)
        profile.balance = Balance.objects.get(user_id=self.request.user.id).amount
        return profile


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'app_users/register.html'
    success_url = reverse_lazy('app_users:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        Balance.objects.create(user=self.object, amount=0)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(
            self.request,
            username=username,
            password=password
        )

        login(request=self.request, user=user)
        return response


class MyLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        logger.info('Запрошена страница аутентификации')
        return super().dispatch(request, args, kwargs)

# def login_view(request: HttpRequest) -> HttpResponse:
#     if request.method == 'GET':
#         logger.info('Запрошена страница аутентификации')
#         if request.user.is_authenticated:
#             return redirect('/admin/')
#
#         return render(request, 'app_users/login.html')
#
#     username = request.POST['username']
#     password = request.POST['password']
#
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/admin/')
#
#     return render(request, 'app_users/login.html', {'error': 'Invalid login credentials'})


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('app_users:login')







