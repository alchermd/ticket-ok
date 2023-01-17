from datetime import timedelta

import pytest
from django.utils import timezone

from authentication.services import create_user
from tickets.services import create_ticket

today = timezone.now()
next_week = today + timedelta(weeks=1)


@pytest.mark.django_db
def test_user_can_create_a_ticket_and_assign_it_to_another_user():
    john = create_user(email="john@example.com")
    jane = create_user(email="jane@example.com")
    ticket = create_ticket(
        created_by=john,
        assigned_to=jane,
        problem_statement="The client is requesting changes for the existing API",
        eta=next_week,
    )
    assert ticket.assigned_to == jane


@pytest.mark.django_db
def test_a_tickets_creation_date_is_autogenerated():
    john = create_user(email="john@example.com")
    jane = create_user(email="jane@example.com")
    ticket = create_ticket(
        created_by=john,
        assigned_to=jane,
        problem_statement="The client is requesting changes for the existing API",
        eta=next_week,
    )
    assert ticket.created_at.day == today.day