# Generated by Django 4.2.2 on 2023-07-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0015_alter_report_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='deadline_status',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
