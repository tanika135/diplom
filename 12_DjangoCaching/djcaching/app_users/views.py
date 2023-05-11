from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.core.cache import cache
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from .forms import BalanceForm
from .models import Profile, Balance


# def user_account(request):
    # return render(request, 'app_users/account.html')

def user_account(request):
    username = request.user.username
    balance = get_balance()

    promotions_cache_key = 'promotions:{}'.format(username)
    offers_cache_key = 'offers:{}'.format(username)
    promotions = get_promotions()
    offers = get_offers()

    user_account_cache_data = {
        promotions_cache_key: promotions,
        offers_cache_key: offers
    }

    cache.set_many(user_account_cache_data)
    payment_history = get_payment_history

    # cache.get_or_set(promotions_cache_key, promotions, 30*60)
    # if promotions_cache_key not in cache:
    #     promotions = get_promotions()
    #     cache.set(promotions_cache_key, promotions, 30*60)

    return render(request, 'users/account.html', context={
        'balance': balance,
        'promotions': promotions,
        'offers': offers,
        'payment_history': payment_history
    })


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
        return super().dispatch(request, args, kwargs)


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('app_users:login')


class BalanceUpdateView(UserPassesTestMixin, UpdateView):
    model = Balance
    template_name_suffix = '_update_form'
    form_class = BalanceForm
    permission_required = 'app_user.change_profile'

    def get_object(self, queryset=None):
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
