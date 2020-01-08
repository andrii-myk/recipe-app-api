from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@mail.ua', password='testpass'):
    """ Create a sample user """
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Should create a new user"""
        email = 'test@mail.ua'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Should check taht email for new user is normalized"""
        email = 'test@MaiL.UA'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Should raise an error when email is empty"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new supersuer"""
        user = get_user_model().objects.create_superuser(
            'test@mail.ua',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ Should test the tag string representation """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan',
        )

        self.assertEqual(str(tag), tag.name)
