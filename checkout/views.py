from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, MakeDonationForm
from .models import OrderLineItem
from django.utils import timezone
from django.conf import settings
from tickets.models import Ticket
import stripe


stripe_api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
  if request.method=='POST':
    order_form = OrderForm(request.POST)
    donation_form = MakeDonationForm(request.POST)

    if order_form.is_valid() and donation_form.is_valid():
      order = order_form.save(commit=False)
      order.date = timezone.now()
      order.save
      ticket = get_object_or_404(Ticket)
      order_line_item = OrderLineItem(
        order = order,
        ticket = ticket,
        donation = donation
      )
      order_line_item.save()
      try:
        customer = stripe.Charge.create(
          amount = int(total * 100),
          currency = "GBP",
          description = request.user.email,
        )

