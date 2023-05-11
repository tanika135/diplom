from datetime import datetime

from django.views.generic import DetailView, ListView
from app_users.models import Balance, Profile
from orders.models import Order
from app_shops.models import Actions, Offers


class AboutMeView(DetailView):

    template_name = 'app_personal/about-me.html'
    model = Profile
    context_object_name = "profile"

    def get_object(self, queryset=None):
        profile = Profile.objects.get(user_id=self.request.user.id)
        profile.balance = Balance.objects.get(user_id=self.request.user.id).amount
        return profile


class OrdersList(ListView):
    template_name = 'app_personal/orders_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.filter(created_by=self.request.user.id)
        return orders


class ActionsList(ListView):
    template_name = 'app_personal/actions_list.html'
    context_object_name = 'actions'

    def get_queryset(self):
        actions = Actions.objects.filter(created_from__lte=datetime.now(), created_to__gte=datetime.now())
        return actions


class OffersList(ListView):
    template_name = 'app_personal/offers_list.html'
    context_object_name = 'offers'

    def get_queryset(self):
        return Offers.objects.filter(active=True)


class BalanceView(DetailView):

    template_name = 'app_personal/balance.html'
    model = Profile
    context_object_name = "profile"

    def get_object(self, queryset=None):
        profile = Profile.objects.get(user_id=self.request.user.id)
        profile.balance = Balance.objects.get(user_id=self.request.user.id).amount
        return profile

