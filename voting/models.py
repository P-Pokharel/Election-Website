from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(blank=False, max_length=120)
    current_position = models.CharField(blank=False, max_length=120)
    desired_position = models.CharField(blank=False, max_length=120)
    date_of_birth = models.DateField(blank=True)
    qualification = models.CharField(blank=True, null=True, max_length=100)
    vote_count = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Voter(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('U', 'Unknown')
    ]

    voter_name = models.CharField(blank=False, max_length=120)
    voter_id = models.CharField(blank=False, max_length=120)
    citizenship_no = models.CharField(blank=False, max_length=120)
    voter_address = models.CharField(blank=False, max_length=120)
    date_of_birth = models.DateField(blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, default='U')
    vote_casted = models.BooleanField(default=False)