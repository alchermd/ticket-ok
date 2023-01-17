from datetime import datetime

from authentication.models import User
from tickets.models import Ticket


def create_ticket(
    *, created_by: User, assigned_to: User, problem_statement: str, eta: datetime
) -> Ticket:
    ticket: Ticket = Ticket.objects.create(
        created_by=created_by,
        assigned_to=assigned_to,
        problem_statement=problem_statement,
        eta=eta,
    )

    return ticket
