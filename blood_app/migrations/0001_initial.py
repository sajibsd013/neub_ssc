# Generated by Django 3.2.8 on 2021-11-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('date_of_birth', models.DateField()),
                ('last_donate', models.DateField()),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Feale', 'Female')], max_length=122)),
                ('blood_type', models.CharField(max_length=12)),
            ],
        ),
    ]
