from django.contrib.auth.models import User
from django.shortcuts import resolve_url
from django.test import TestCase

from django_ajax.bookings.models import Booking


class TestHtml(TestCase):
    def setUp(self):
        Booking.objects.create(
            user=User.objects.create_user('johndoe', password='jd'),
            event='Pride',
            date='2014-12-27'
        )


class TestGetNoDate(TestHtml):

    def setUp(self):
        super().setUp()
        self.resp = self.client.get(resolve_url('booking:list'))

    def test_status(self):
        self.assertEqual(200, self.resp.status_code)

    def test_content(self):
        self.assertNotIn('Pride', self.resp.content.decode('utf-8'))


class TestGetWithDate(TestHtml):

    def setUp(self):
        super().setUp()
        url = resolve_url('booking:date', month=12, year=2014)
        self.resp = self.client.get(url)

    def test_status(self):
        self.assertEqual(200, self.resp.status_code)

    def test_content(self):
        content = self.resp.content.decode('utf-8')
        with self.subTest():
            self.assertIn('Dezembro 2014', content)
            self.assertIn('Pride', content)
