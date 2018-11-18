from django import forms
from .models import Ticket


class CommentForm(forms.Form):
  comment = forms.CharField(required=True, widget=forms.Textarea)

class TicketForm(forms.ModelForm):

  class Meta:
    model = Ticket
    fields = ('title', 'text',)