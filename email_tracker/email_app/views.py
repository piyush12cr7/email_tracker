from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import EmailForm
from .models import Email, EmailTracker


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            recipients = form.cleaned_data['recipients'].split(',')
            send_mail(subject, body, 'your_email@example.com', recipients)
            email = Email(subject=subject, body=body)
            email.save()
            return redirect('email_sent.html')
    else:
        form = EmailForm()

    return render(request, 'email_app/send_email.html', {'form': form})


def email_sent(request):
    return render(request, 'email_app/email_sent.html')
