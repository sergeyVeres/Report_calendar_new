# Generated by Django 4.2.2 on 2023-06-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='comment',
            field=models.CharField(blank=True, max_length=300, verbose_name='комментарий'),
        ),
    ]