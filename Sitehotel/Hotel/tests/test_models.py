from django.test import TestCase

from Hotel.models import *

# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass
#
#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass
#
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)
#
#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)
# python manage.py test
#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)


class RoomModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        t = Type.objects.create(type='girl')
        Room.objects.create(type=t, slug='girl', description='good', area=15, price=1000, capacity=2)

    def test_descriotion_max_length(self):
        room = Room.objects.get(id=1)
        field_label = room._meta.get_field('description').max_length
        self.assertEqual(field_label, 500)

    def test_object_name_is_type(self):
        room = Room.objects.get(id=1)
        expected_object_name = f'{room.type}'
        self.assertEqual(str(room), expected_object_name)

    def test_get_absolute_url(self):
        room = Room.objects.get(id=1)
        self.assertEqual(room.get_absolute_url(), '/Room/girl/')


class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        g = Grade.objects.create(grade=2)
        Review.objects.create(first_name='Grag', surname='Lala', grade=g, text='blabla')

    def test_text_max_length(self):
        rev = Review.objects.get(id=1)
        field_label = rev._meta.get_field('text').max_length
        self.assertEqual(field_label, 2000)

    def test_object_name_is_expected(self):
        rev = Review.objects.get(id=1)
        expected_object_name = f'{rev.surname}  {rev.first_name}'
        self.assertEqual(str(rev), expected_object_name)