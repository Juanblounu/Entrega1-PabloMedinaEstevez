from django.shortcuts import redirect, render
from datetime import datetime
from .forms import FormTeam, TeamSearch
from .models import Team

def home_page(request):
    return render(request, 'index.html')

def create_team(request):
    if request.method == 'POST':
        form = FormTeam(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('creation_date')
            if not fecha:
                fecha = datetime.now() 
            
            team = Team(
                team_name=data.get('team_name'),
                principal_player=data.get('principal_player'),
                creation_date=fecha
            )
            team.save()

            
            return redirect('teams_list')
        
        else:
            return render(request, 'create_team.html', {'form': form})
            
    
    form_team = FormTeam()
    
    return render(request, 'create_team.html', {'form': form_team})


def teams_list(request):
    
    search_name = request.GET.get('team_name')
    
    if search_name:
        teams_list = Team.objects.filter(team_name__icontains=search_name) 
    else:
        teams_list = Team.objects.all()
    
    form = TeamSearch()
    return render(request, 'teams_list.html', {'teams_list': teams_list, 'form': form})


def about_me(request):
    return render(request, 'about_me.html')