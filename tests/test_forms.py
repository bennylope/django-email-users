import unittest
from django.utils import timezone
from users.forms import UserCreationForm, UserChangeForm
from users.models import User


class TestForms(unittest.TestCase):

    def setUp(self):
        defaults = {'password': "pass", "last_login": timezone.now(),
                "date_joined": timezone.now()}
        self.user, _ = User.objects.get_or_create(
            email="test@test.co", defaults=defaults,
        )
        self.other, _ = User.objects.get_or_create(
            email="other@test.co", defaults=defaults,
        )

    def test_create_unique(self):
        """Ensure basic data validates"""
        form = UserCreationForm(data={
            'email': 'new@blah.com',
            'password1': 'pass',
            'password2': 'pass',
        })
        self.assertTrue(form.is_valid())

    def test_create_duplicate(self):
        """Ensure an existing email address results in an error"""
        form = UserCreationForm(data={
            'email': 'test@test.co',
            'password1': 'new',
            'password2': 'new',
        })
        self.assertFalse(form.is_valid())

    def test_create_icase_duplicate(self):
        """Ensure email validation is case insensitive"""
        form = UserCreationForm(data={
            'email': 'Test@Test.co',
            'password1': 'new',
            'password2': 'new',
        })
        self.assertFalse(form.is_valid())

    def test_change_email(self):
        """Ensure resupplying the email address raises no error"""
        form = UserChangeForm(instance=self.user, data={
            'email': 'test@test.co',
            'date_joined': '2011-01-01',
            'last_login': '2011-01-01',
        })
        self.assertTrue(form.is_valid())

    def test_change_other_email(self):
        """Ensure supplying someone else's email raises error"""
        form = UserChangeForm(instance=self.other, data={
            'email': 'test@test.co',
            'date_joined': '2011-01-01',
            'last_login': '2011-01-01',
        })
        self.assertFalse(form.is_valid())
