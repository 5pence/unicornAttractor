"""
This module handles the view functionality of everything in the
pages that relate to tickets
"""
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils import timezone
from .models import Ticket, Vote, Comments
from .form import CommentForm, TicketForm


def post_ticket_list(request):
    """Gets the tickets, sorts and orders them ready for view"""
    features = Ticket.objects.filter(
        created_date__lte=timezone.now(),
        ticket_type=Ticket.FEATURE).order_by('-money_raised')
    bugs = Ticket.objects.filter(created_date__lte=timezone.now(), ticket_type=Ticket.BUG)
    vote_dict = {}
    if request.user:
        votes = Vote.objects.filter(user=request.user)
        for v in votes:
            vote_dict[v.ticket_id] = True
    bugs = [(b, b.id in vote_dict) for b in bugs]
    return render(request, 'tickets/ticket_list.html', {'features': features, 'bugs': bugs, 'votes': vote_dict})


def ticket_donation(request):
    """
    Increases money_raised of feature by 20 pounds
    and redirects back to the same page
    """
    ticket_number = request.GET.get('id')
    next_page = "ticket_single?id=" + str(ticket_number)
    if "next" in request.GET:
        next_page = request.GET.get('next')
    ticket = Ticket.objects.get(id=request.GET.get('id'))
    ticket.money_raised += 20
    ticket.save()
    return HttpResponseRedirect(next_page)


def ticket_vote(request):
    """
    Increments vote count of bug and redirects back
    to the same page
    """
    ticket_number = request.GET.get('id')
    next_page = "ticket_single?id=" + str(ticket_number)
    if "next" in request.GET:
        next_page = request.GET.get('next')
    bug = Ticket.objects.get(id=ticket_number)
    user = request.user
    vote = Vote(user=user, ticket=bug)
    vote.save()
    return HttpResponseRedirect(next_page)


def ticket_single(request):
    """
    Gets the single ticket and preps data for single ticket 
    page. Also handles voting on single ticket page
    """
    ticket = Ticket.objects.get(id=request.GET.get('id'))
    form = CommentForm()
    try:
        vote = Vote.objects.get(ticket=ticket, user=request.user)
    except Vote.DoesNotExist:
        vote = None
    if 'comment' in request.POST:
        comment = request.POST.get("comment")
        comment = Comments(user=request.user, ticket=ticket, comment=comment)
        comment.save()
    comments_already_posted = Comments.objects.filter(ticket=ticket)

    is_voted_by_user = False
    if vote:
        is_voted_by_user = True
    return render(
        request, 'tickets/ticket_single.html', {
            'ticket': ticket,
            'voted': is_voted_by_user,
            'form': form,
            'comments': comments_already_posted})


def ticket_create(request):
    """
    Ensures create ticket form is valid and pushes data into
    a new ticket, then redirects to ticket list page
    """
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.created_date = timezone.now()
            ticket.ticket_status = Ticket.TODO
            ticket.ticket_type = Ticket.BUG
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_create.html', {'form': form})
