import pytest

from authentication.models import User
from authentication.services import create_user


@pytest.mark.django_db
def test_can_create_a_user():
    user = create_user(email="john@example.com")
    assert type(user) == User
