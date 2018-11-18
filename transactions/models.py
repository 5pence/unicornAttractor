from django.db import models
from django.utils import timezone
from tickets.models import Ticket
from users.models import User


class Transaction(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    amount = models.IntegerField(null=True, blank=True)