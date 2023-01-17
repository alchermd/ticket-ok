from authentication.models import User


def create_user(*, email: str) -> User:
    user: User = User.objects.create(email=email)

    return user
