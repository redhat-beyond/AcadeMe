from django import forms
from .models import Messages, MessageBoards


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = "__all__"
