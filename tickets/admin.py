from django.contrib import admin
from .models import Ticket, Vote, Comments

class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'ticket','date_voted')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'completed_date', 'ticket_status', 'ticket_type', 'money_raised')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Comments)
