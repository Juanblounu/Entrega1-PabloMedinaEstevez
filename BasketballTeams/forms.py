from django import forms
from ckeditor.fields import RichTextFormField

class FormTeam(forms.Form):
    team_name = forms.CharField(max_length=30)
    principal_player = forms.CharField(max_length=30)
    description = RichTextFormField()
    image = forms.ImageField(required=False)
    creation_date = forms.DateField(required=False)
    
class TeamSearch(forms.Form):
    team_name = forms.CharField(max_length=30, required=False)