from django.contrib.auth.models import User

from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Start demo select fields')

        """
        Вернёт кортеж. Если добавить flat=True, то вернет список без вложенных кортежей
        """

        users_info = User.objects.values_list('pk', 'username')
        for u_info in users_info:
            print(u_info)
        """
        Вернёт словарь
        """
        # products_values = Product.objects.values('pk', 'name')
        # for p_values in products_values:
        #     print(p_values)

        self.stdout.write(f'Done')
