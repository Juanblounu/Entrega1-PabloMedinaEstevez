# Generated by Django 4.0.6 on 2022-08-03 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BasketballTeams', '0004_team_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='user',
        ),
    ]
