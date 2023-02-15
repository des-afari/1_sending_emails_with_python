from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.mail import send_mail
from django.contrib import messages 


def index(request):
    if request.method == 'GET':
        email_form = EmailForm()

        payload = {
            "email_form": email_form
        }

        return render(request, 'index.html', payload)

    elif request.method == 'POST':
        email_form = EmailForm(request.POST)

        if email_form.is_valid():
            sender = email_form.cleaned_data['sender']

            recipients = email_form.cleaned_data['recipients']
            recipient_list = list(recipients.split(';'))

            subject = email_form.cleaned_data['subject']
            message = email_form.cleaned_data['message']


        try:
            send_mail(subject, message, sender, recipient_list, fail_silently=False)
            return redirect('success.html')
        
        except:
            messages.error(request, 'Failed to send message')
            return redirect('/')
        



