from datetime import datetime

from authentication.models import User
from tickets.exceptions import UserNotTheAssignedQA
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


def assign_qa(*, ticket: Ticket, qa: User) -> Ticket:
    ticket.assigned_qa = qa
    ticket.save()

    return ticket


def mark_ticket_as(*, ticket: Ticket, qa: User, status: Ticket.QAStatus) -> Ticket:
    if qa is not ticket.assigned_qa:
        raise UserNotTheAssignedQA

    ticket.qa_status = status
    ticket.save()

    return ticket
