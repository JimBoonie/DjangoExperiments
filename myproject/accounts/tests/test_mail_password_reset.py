from django.core import mail
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

class PasswordResetMailTests(TestCase):
    def setUp(self):
        self.username = 'john'
        self.emailaddress = 'john@doe.com'
        User.objects.create_user(username=self.username, email=self.emailaddress, password='123abcdef')
        self.response = self.client.post(reverse('password_reset'), {'email': self.emailaddress})
        self.email = mail.outbox[0]

    def test_email_subject(self):
        self.assertEquals('[Django Boards] Please reset your password', self.email.subject)

    def test_email_body(self):
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_reset_token_url = reverse('password_reset_confirm', kwargs={
            'token': token,
            'uidb64': uid,
        })
        self.assertIn(password_reset_token_url, self.email.body)
        self.assertIn(self.username, self.email.body)
        self.assertIn(self.emailaddress, self.email.body)

    def test_email_to(self):
        self.assertEqual([self.emailaddress,], self.email.to)