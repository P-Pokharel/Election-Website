from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(blank=False, max_length=120)
    current_position = models.CharField(blank=False, max_length=120)
    desired_position = models.CharField(blank=False, max_length=120)
    date_of_birth = models.DateField(blank=True)
    qualification = models.CharField(blank=True, null=True, max_length=100)
    vote_count = models.IntegerField(default=0)