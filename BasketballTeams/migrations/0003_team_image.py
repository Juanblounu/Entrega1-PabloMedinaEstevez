# Generated by Django 4.0.6 on 2022-08-03 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasketballTeams', '0002_team_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagen'),
        ),
    ]
