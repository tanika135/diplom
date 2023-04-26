import json
from django.test import TestCase
from django.urls import reverse


class GetCookieViewTestCase(TestCase):
    def test_get_cookie_view(self):
        response = self.client.get(reverse('myauth:cookie-get'))
        self.assertContains(response, 'Cookie value')


class FooBarViewTest(TestCase):
    def test_foo_bar_view(self):
        response = self.client.get(reverse('myauth:foo-bar'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.headers['content-type', 'aplication/json'],
        )
        expected_data = {'spam': 'eggs', 'foo': 'bar'}
        # received_data = json.loads(response.content)
        # self.assertEquals(received_data, expected_data)
        self.assertJSONEqual(response.content, expected_data)
