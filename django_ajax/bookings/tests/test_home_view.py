from django.shortcuts import resolve_url
from django.test import TestCase


class TestGet(TestCase):

    def setUp(self):
        self.resp = self.client.get(resolve_url('home'))

    def test_status(self):
        self.assertEqual(200, self.resp.status_code)

    def test_content(self):
        content = self.resp.content.decode('utf-8')
        with self.subTest():
            self.assertIn('/api/bookings/', content)
            self.assertIn('/bookings/', content)
