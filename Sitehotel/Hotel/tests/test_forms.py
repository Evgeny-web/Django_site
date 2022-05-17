import datetime
from django.test import TestCase
from django.utils import timezone

from Hotel.forms import *


# python manage.py test Hotel.tests.test_forms
class RentRoomFormTest(TestCase):
    def test_rent_room_fields_help_text(self):
        form = RentRoom()
        self.assertEqual(form.fields['birthday'].help_text, 'Example: 2022-05-05')
        self.assertEqual(form.fields['arrival_date'].help_text, 'Example: 2022-05-05')
        self.assertEqual(form.fields['date_of_departure'].help_text, 'Example: 2022-05-05')

    def test_rent_room_arrival_date_in_past(self):
        dat = datetime.date.today() - datetime.timedelta(days=1)
        t = Type.objects.create(type='girl')
        p = PayMethod.objects.create(pay_type='cash')
        r = Room.objects.create(type=t, slug='girl', description='good', area=15, price=1000, capacity=2)
        form = RentRoom(data=
        {
            'first_name': 'Grag', 'surname': 'Gr', 'birthday': '2001-02-21', 'reservation_room': r,
            'arrival_date': dat, 'date_of_departure': datetime.date.today()+datetime.timedelta(days=1), 'phone_number': '234',
            'email': 'ttt@mail.ru', 'pay_method': p
        })
        self.assertFalse(form.is_valid())

    def test_rent_room_date_of_departure_in_future(self):
        dat = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        t = Type.objects.create(type='girl')
        p = PayMethod.objects.create(pay_type='cash')
        r = Room.objects.create(type=t, slug='girl', description='good', area=15, price=1000, capacity=2)
        form = RentRoom(data=
        {
            'first_name': 'Grag', 'surname': 'Gr', 'birthday': '2001-02-21', 'reservation_room': r,
            'arrival_date': datetime.date.today(), 'date_of_departure': dat,
            'phone_number': '234',
            'email': 'ttt@mail.ru', 'pay_method': p
        })
        self.assertFalse(form.is_valid())

    def test_rent_room_arrival_date_today(self):
        dat = datetime.date.today()
        t = Type.objects.create(type='girl')
        p = PayMethod.objects.create(pay_type='cash')
        r = Room.objects.create(type=t, slug='girl', description='good', area=15, price=1000, capacity=2)
        form = RentRoom(data=
        {
            'first_name': 'Grag', 'surname': 'Gr', 'birthday': '2001-02-21', 'reservation_room': r,
            'arrival_date': dat, 'date_of_departure': datetime.date.today()+datetime.timedelta(days=1),
            'phone_number': '234',
            'email': 'ttt@mail.ru', 'pay_method': p
        })
        self.assertTrue(form.is_valid())

    def test_rent_room_date_of_departure_max(self):
        dat = datetime.date.today() + datetime.timedelta(weeks=4)
        t = Type.objects.create(type='girl')
        p = PayMethod.objects.create(pay_type='cash')
        r = Room.objects.create(type=t, slug='girl', description='good', area=15, price=1000, capacity=2)
        form = RentRoom(data=
        {
            'first_name': 'Grag', 'surname': 'Gr', 'birthday': '2001-02-21', 'reservation_room': r,
            'arrival_date': datetime.date.today(), 'date_of_departure': dat,
            'phone_number': '234',
            'email': 'ttt@mail.ru', 'pay_method': p
        })
        self.assertTrue(form.is_valid())

    def test_rent_room_date_of_departure_today(self):
        dat = datetime.date.today()
        t = Type.objects.create(type='girl')
        p = PayMethod.objects.create(pay_type='cash')
        r = Room.objects.create(type=t, slug='girl', description='good', area=15, price=1000, capacity=2)
        form = RentRoom(data=
        {
            'first_name': 'Grag', 'surname': 'Gr', 'birthday': '2001-02-21', 'reservation_room': r,
            'arrival_date': datetime.date.today(), 'date_of_departure': dat,
            'phone_number': '234',
            'email': 'ttt@mail.ru', 'pay_method': p
        })
        self.assertFalse(form.is_valid())
