# Generated by Django 5.0.1 on 2024-05-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('current_position', models.CharField(max_length=120)),
                ('desired_position', models.CharField(max_length=120)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
