# Generated by Django 5.0.1 on 2024-07-05 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0008_remove_candidate_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='user',
        ),
    ]
