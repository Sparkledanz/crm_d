# Generated by Django 4.1.7 on 2023-03-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_employee_date_employer_date_partner_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='notes',
            field=models.CharField(max_length=200),
        ),
    ]
