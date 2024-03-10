import pytest

from users.forms import UserCreationForm, UserChangeForm
from users.models import User


pytestmark = pytest.mark.django_db


@pytest.fixture
def users():
    user = User.objects.create(
        email="test@test.co",
        password="pass",
    )
    other = User.objects.create(
        email="other@test.co",
        password="pass",
    )
    return user, other


def test_new_user_data_validates(users):
    """Ensure basic data validates"""
    form = UserCreationForm(
        data={
            "email": "new@blah.com",
            "password1": "pass",
            "password2": "pass",
        }
    )
    assert form.is_valid()


@pytest.mark.parametrize("email", ["test@test.co", "Test@Test.co"])
def test_cannot_create_user_with_duplicate_email(users, email):
    """Case insensitive email check"""

    form = UserCreationForm(
        data={
            "email": email,
            "password1": "new",
            "password2": "new",
        }
    )
    assert not form.is_valid()


def test_existing_user_can_change_email(users):
    """Ensure resupplying the email address raises no error"""
    user, other = users
    form = UserChangeForm(
        instance=user,
        data={
            "email": "test@test.co",
            "date_joined": "2011-01-01",
            "last_login": "2011-01-01",
        },
    )
    assert form.is_valid()


def test_existing_user_cannot_change_to_other_existing_email(users):
    """Ensure supplying someone else's email raises error"""
    user, other = users
    form = UserChangeForm(
        instance=other,
        data={
            "email": "test@test.co",
            "date_joined": "2011-01-01",
            "last_login": "2011-01-01",
        },
    )
    assert not form.is_valid()
