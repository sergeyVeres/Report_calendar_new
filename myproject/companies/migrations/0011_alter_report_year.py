# Generated by Django 4.2.2 on 2023-07-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_report_period_report_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='year',
            field=models.CharField(choices=[('2023', '2023'), ('2024', '2024')], max_length=20, verbose_name='Год отчета'),
        ),
    ]
