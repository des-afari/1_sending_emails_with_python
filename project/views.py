from django.shortcuts import render
from .forms import EmailForm


def index(request):
    email_form = EmailForm()

    payload = {
        "email_form": email_form
    }
    return render(request, 'index.html', payload)


