from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages 
from . forms import EmailForm


def index(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST)

        if email_form.is_valid():
            sender = email_form.cleaned_data['sender']

            recipients = email_form.cleaned_data['recipients']
            recipient_list = list(recipients.split(';'))

            subject = email_form.cleaned_data['subject']
            message = email_form.cleaned_data['message']


            try:
                send_mail(subject, message, sender, recipient_list, fail_silently=False)
                return redirect('success')

            except:
                messages.error(request, 'Failed to send message')
                return redirect('/')
        
        else:
                messages.error(request, 'Invalid form data')
                return redirect('/')
            
    else:
        email_form = EmailForm()

        return render(request, 'index.html', {'email_form': email_form})
        

success = lambda request: render(request, 'success.html')

