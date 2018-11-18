from django.db import models
from django.utils import timezone
from tickets.models import Ticket

class Order(models.Model):
  full_name = models.CharField(max_length=50, blank=False)
  phone_number = models.CharField(max_length=20, blank=False)
  country = models.CharField(max_length=50, blank=False)
  postcode = models.CharField(max_length=20, blank=True)
  town_or_city = models.CharField(max_length=50, blank=False)
  street_address1 = models.CharField(max_length=50, blank=False)
  street_address2 = models.CharField(max_length=50, blank=True)
  county = models.CharField(max_length=50, blank=False)
  date = models.DateField(default=timezone.now)

  def __str__(self):
    return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

class OrderLineItem(models.Model):
  order = models.ForeignKey(Order, null=False, on_delete=models.DO_NOTHING)
  ticket = models.ForeignKey(Ticket, null=False, on_delete=models.DO_NOTHING)
  donation = models.IntegerField(blank=False, default=10)

  def __str__(self):
    return "£{0} donation for ticket {1} - {2}".format(self.donation, self.ticket.id, self.ticket.title)
