# Generated by Django 5.0.1 on 2024-07-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0010_voter_vote_casted'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='citizenship_no',
            field=models.CharField(default=123456789, max_length=120),
            preserve_default=False,
        ),
    ]
