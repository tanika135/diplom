from django.test import TestCase
from django.urls import reverse
from django.utils import translation


class WelcomeTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        translation.activate('ru')

    def test_welcome(self):
        response = self.client.get(reverse('app_pages:welcome'))
        self.assertTemplateUsed(response, 'app_pages/welcome.html')

    def test_welcome(self):
        response = self.client.get(reverse('app_pages:main'))
        self.assertTemplateUsed(response, 'app_pages/main.html')
