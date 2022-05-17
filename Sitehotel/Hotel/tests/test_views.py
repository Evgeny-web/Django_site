import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from Hotel.models import *


# python manage.py test Hotel.tests.test_views
class ReviewListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create 8 reviews for pagination tests
        number_of_reviews = 8
        Grade.objects.create(grade=1)

        for review_id in range(number_of_reviews):
            Review.objects.create(
                first_name=f'Bob {review_id}',
                surname=f'Surname {review_id}',
                grade=Grade.objects.get(id=1),
                text='dsfsdf'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/review/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Hotel/reviews.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['rev']), 5)

    def test_lists_all_reviews(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('reviews') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['rev']), 3)


# python manage.py test Hotel.tests.test_views.LoanedAddRoomByUserCreateViewTest
class LoanedAddRoomByUserCreateViewTest(TestCase):
    def setUp(self):
        # create user
        test_user1 = User.objects.create_user(username='testuser1', password='1xx2fdsjksf')

        test_user1.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('add_room'))
        self.assertRedirects(response, '/login/?next=/add_room/')

    def test_logged_in_uses_correcr_template(self):
        login = self.client.login(username='testuser1', password='1xx2fdsjksf')
        response = self.client.get(reverse('add_room'))

        # check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # check we used correct template
        self.assertTemplateUsed(response, 'Hotel/addroom.html')

