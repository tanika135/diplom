from django.test import TestCase
from django.urls import reverse


class WelcomeTestCase(TestCase):
    def test_welcome(self):
        response = self.client.get(reverse('app_pages:welcome'))
        self.assertTemplateUsed(response, 'app_pages/welcome.html')


class MainPageTestCase(TestCase):
    def test_welcome(self):
        response = self.client.get(reverse('app_pages:main'))
        self.assertTemplateUsed(response, 'app_pages/main.html')

