from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)
    recipients = forms.CharField(widget=forms.Textarea)