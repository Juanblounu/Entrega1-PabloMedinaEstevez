from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Team(models.Model):
    team_name = models.CharField(max_length=30)
    principal_player = models.CharField(max_length=30)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to='imagen', null=True, blank=True)
    creation_date = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.team_name}'