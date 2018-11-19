"""Builder for tickett and comment forms """
from django import forms
from .models import Ticket


class CommentForm(forms.Form):
    """Form for creating comments"""
    comment = forms.CharField(required=True, widget=forms.Textarea)


class TicketForm(forms.ModelForm):
    """Form for creating ticekts"""

    class Meta:
        """Form for creating ticekts, we only need title and text"""
        model = Ticket
        fields = ('title', 'text')
