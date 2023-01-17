from django.db import models

from authentication.models import User


class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="created_tickets", on_delete=models.CASCADE
    )
    assigned_to = models.ForeignKey(
        User, related_name="assigned_tickets", on_delete=models.CASCADE
    )
    problem_statement = models.TextField()
    eta = models.DateTimeField()
    assigned_qa = models.ForeignKey(
        User, related_name="assigned_tickets_as_qa", on_delete=models.CASCADE, null=True
    )
