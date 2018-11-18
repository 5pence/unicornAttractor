from django.db import models
from django.utils import timezone
from users.models import User


class Ticket(models.Model):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'
    BUG = 'bug'
    FEATURE = 'feature'
    TICKET_STATUS_CHOICES = (
        (TODO, 'todo'),
        (DOING, 'doing'),
        (DONE, 'done')
    )
    TICKET_TYPE_CHOICES = (
        (BUG, 'bug'),
        (FEATURE, 'feature')
    )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)
    ticket_status = models.CharField(max_length=5, choices=TICKET_STATUS_CHOICES, default=TODO)
    ticket_type = models.CharField(max_length=7, choices=TICKET_TYPE_CHOICES, default=FEATURE)
    votes = models.ManyToManyField(User, through='Vote', related_name='voter')
    money_raised = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_voted = models.DateTimeField(default=timezone.now)
    class Meta:
        unique_together = (('user', 'ticket'), )

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=2000, blank=False)
        