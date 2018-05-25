
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

    def test_post_item_to_view_and_redirect_to_index_page(self):
        resp = self.client.post("/", {})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, "/")

    def test_post_item_to_view_and_retrieve_it(self):
        resp = self.client.post("/", data={
            "new_item": "do it now",
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "do it now")
