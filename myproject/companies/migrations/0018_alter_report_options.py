# Generated by Django 4.2.2 on 2023-07-09 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0017_alter_report_deadline_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['deadline']},
        ),
    ]
