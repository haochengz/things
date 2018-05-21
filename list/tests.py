
from django.test import TestCase
from django.urls import resolve

from .views import index_page


class SomeTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_url_resolve(self):
        found = resolve('/')
        self.assertEqual(found.func, index_page)
