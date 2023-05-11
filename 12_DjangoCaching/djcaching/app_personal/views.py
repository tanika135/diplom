from django.views.generic import DetailView
from app_users.models import Balance, Profile


class AboutMeView(DetailView):

    template_name = 'app_personal/about-me.html'
    model = Profile
    context_object_name = "profile"

    def get_object(self, queryset=None):
        profile = Profile.objects.get(user_id=self.request.user.id)
        profile.balance = Balance.objects.get(user_id=self.request.user.id).amount
        return profile
