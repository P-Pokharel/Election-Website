# Generated by Django 5.0.1 on 2024-05-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='qualification',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='vote_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
    ]
