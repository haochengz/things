
from django.test import TestCase


class SomeTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fail(self):
        self.fail("Unit test runs")
