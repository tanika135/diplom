from django.views.generic import DetailView, ListView

from app_users.models import Balance, Profile
from orders.models import Order


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
    queryset = Order.objects.all()
