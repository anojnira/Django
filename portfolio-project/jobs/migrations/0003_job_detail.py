# Generated by Django 4.1.5 on 2023-02-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='detail',
            field=models.TextField(null=True),
        ),
    ]