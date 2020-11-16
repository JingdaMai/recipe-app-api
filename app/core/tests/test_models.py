from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        # username = 'mai'
        email = 'mai@a.com'
        password = 'test8888'

        user = get_user_model().objects.create_user(
            # username=username,
            email=email,
            password=password
        )

        # self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'mai@A.com'
        user = get_user_model().objects.create_user(email, 'test8888')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test8888')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@a.com',
            'test8888'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
