# Generated by Django 5.0.1 on 2024-05-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_candidate_qualification_candidate_vote_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='qualification',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]