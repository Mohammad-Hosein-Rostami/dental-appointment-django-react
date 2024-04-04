from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('doctor', 'Doctor'),
        ('regular', 'Regular'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='regular')
    name = models.CharField(max_length=255)
    cellphone = models.CharField(max_length=20)
    # The username and password fields come from AbstractUser.


class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_profile')
    # Additional doctor-specific fields can go here, if any.
    # For now, we'll assume all specific fields are covered by the User model.
    def __str__(self):
        return self.user.username


class Review(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='given_reviews', limit_choices_to={'user_type': 'doctor'})
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_reviews', limit_choices_to={'user_type': 'regular'})
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Time(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='times', limit_choices_to={'user_type': 'doctor'})
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='reserved_times', limit_choices_to={'user_type': 'regular'})
    dateTime = models.DateTimeField()
    available = models.BooleanField(default=True)
    text = models.TextField(blank=True, null=True)