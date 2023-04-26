from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(pk=1)
        group, created = Group.objects.get_or_create(
            name='profile_manager',
        )
        permission_profile = Permission.objects.get(
            codename='view_profile',
        )
        permission_logentry = Permission.objects.get(
            codename='view_logentry',
        )

        #добавление разрешения в группу
        group.permissions.add(permission_profile)

        #присоединение пользоователя к группе
        user.groups.add(group)

        #связать пользователя напрямую к разрешениею
        user.user_permissions.add(permission_logentry)

        group.save()
        user.save()
