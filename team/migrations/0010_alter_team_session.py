# Generated by Django 3.2.8 on 2021-11-03 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_committee_list_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.committee_list'),
        ),
    ]
