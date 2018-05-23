
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import index_page


class SomeTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_url_resolve(self):
        found = resolve('/')
        self.assertEqual(found.func, index_page)

    def test_index_view_returns_html_page(self):
        request = HttpRequest()
        response = index_page(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn("<title>To-do Things</title>", response.content.decode())
        self.assertTrue(response.content.endswith(b'</html>'))
