# Generated by Django 3.2.8 on 2021-11-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_app', '0006_alter_blood_donor_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_donor',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='blood_donor',
            name='last_donate',
            field=models.DateField(),
        ),
    ]