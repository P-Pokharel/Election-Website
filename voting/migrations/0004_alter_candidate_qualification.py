# Generated by Django 5.0.1 on 2024-05-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_alter_candidate_qualification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='qualification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]