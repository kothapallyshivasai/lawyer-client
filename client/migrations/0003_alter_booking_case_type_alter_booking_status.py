# Generated by Django 5.0.3 on 2024-04-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_booking_case_type_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='case_type',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.BooleanField(),
        ),
    ]
