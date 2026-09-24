from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class CustomerRecordViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test-user',
            password='test-password',
        )
        self.client.force_login(self.user)

    def test_missing_record_redirects_home(self):
        response = self.client.get(reverse('record', args=[999]))

        self.assertRedirects(
            response,
            reverse('home'),
            fetch_redirect_response=False,
        )
        home_response = self.client.get(reverse('home'))
        self.assertContains(home_response, 'Record not found.')
