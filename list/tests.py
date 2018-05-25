
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import IndexView


class SomeTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_url_resolve(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, IndexView)

    def test_index_view_returns_html_page(self):
        resp = self.client.get("/")
        self.assertTemplateUsed(resp, "index.html")
