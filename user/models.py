from django.db import models
from django import forms

# Create your models here.

class User(models.Model):
    STATUS_CHOICES = (
        ("ACT", "ACTIVE"),
        ("BAN", "BANNED")
    )

    id = models.UUIDField(auto_created=True, unique=True, editable=False, primary_key=True)
    first_name = models.CharField(max_length=39, null=False, blank=False)
    last_name = models.CharField(max_length=39, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False, unique=True)
    password = forms.CharField(max_length=39, widget=forms.PasswordInput)
    date_birth = models.DateField()
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name