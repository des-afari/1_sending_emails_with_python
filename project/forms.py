import os
from django import forms


class EmailForm(forms.Form):
    sender = forms.CharField(label='', max_length=200, initial=os.getenv('email'), widget=forms.TextInput(attrs={'placeholder': 'Sender'}))
    recipient = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Recipient'}))
    subject = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Message'}))
