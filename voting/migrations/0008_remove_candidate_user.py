# Generated by Django 5.0.1 on 2024-07-05 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_candidate_user_voter_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='user',
        ),
    ]
