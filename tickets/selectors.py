from typing import List

from authentication.models import User
from tickets.models import Ticket


def get_assigned_tickets(*, user: User) -> List[Ticket]:
    tickets: List[Ticket] = Ticket.objects.filter(assigned_to=user)
    return tickets


def get_created_tickets(*, user: User) -> List[Ticket]:
    tickets: List[Ticket] = Ticket.objects.filter(created_by=user)
    return tickets


def get_assigned_qa_tickets(*, user: User) -> List[Ticket]:
    tickets: List[Ticket] = Ticket.objects.filter(assigned_qa=user)
    return tickets
