from django.contrib.auth.models import User
from django.test import TestCase

from django_ajax.bookings.models import Booking


URL = '/api/bookings/'
USERNAME = 'johdoe'
PASSWORD = 'jd'


class TestGet(TestCase):

    def setUp(self):
        Booking.objects.create(
            user=User.objects.create_user(USERNAME, password=PASSWORD),
            event='Pride',
            date='2016-12-27'
        )

    def test_status_without_login(self):
        resp = self.client.get(URL)
        self.assertEqual(403, resp.status_code)

    def test_status_logged(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        resp = self.client.get(URL)
        self.assertEqual(200, resp.status_code)


class TestPost(TestCase):

    def setUp(self):
        User.objects.create_user(USERNAME, password=PASSWORD)
        self.data = {
            'user': 1,
            'event': 'Pride',
            'date': '2016-12-27'
        }

    def test_status_without_login(self):
        resp = self.client.post(URL, data=self.data)
        self.assertEqual(403, resp.status_code)

    def test_post_with_invalid_data(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        self.data.update({
            'user': 'johndoe',
            'date': 'Today'
        })
        resp = self.client.post(URL, data=self.data)
        self.assertEqual(400, resp.status_code)

    def test_status_logged(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        resp = self.client.post(URL, data=self.data)
        self.assertEqual(201, resp.status_code)

    def test_create(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        self.client.post(URL, data=self.data)
        self.assertEqual(1, Booking.objects.count())
