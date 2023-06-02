from django.db import models


class Email(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    opened = models.BooleanField(default=False)


class EmailTracker(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    open_date = models.DateTimeField(null=True, blank=True)