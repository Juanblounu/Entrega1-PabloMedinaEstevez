from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=30)
    principal_player = models.CharField(max_length=30)
    creation_date = models.DateField(null=True)
    
    def __str__(self):
        return f'Name of the team: {self.team_name}'