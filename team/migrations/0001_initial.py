# Generated by Django 3.2.8 on 2021-11-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('position', models.CharField(max_length=122)),
                ('session', models.CharField(max_length=122)),
                ('img', models.CharField(max_length=122)),
            ],
        ),
    ]
