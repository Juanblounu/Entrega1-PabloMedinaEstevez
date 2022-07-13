from django import forms

class FormTeam(forms.Form):
    team_name = forms.CharField(max_length=30)
    principal_player = forms.CharField(max_length=30)
    creation_date = forms.DateField(required=False)
    
class TeamSearch(forms.Form):
    team_name = forms.CharField(max_length=30, required=False)