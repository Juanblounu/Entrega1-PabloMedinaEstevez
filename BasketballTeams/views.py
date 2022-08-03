from django.shortcuts import redirect, render

from datetime import datetime
from .forms import FormTeam, TeamSearch
from .models import Team
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

def home_page(request):
    return render(request, 'index.html')

def create_team(request):
    
    if request.method == 'POST':
        form = FormTeam(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('creation_date')
            if not fecha:
                fecha = datetime.now() 
            
            team = Team(
                team_name=data.get('team_name'),
                principal_player=data.get('principal_player'),
                description=data.get('description'),
                image=data.get('image'),
                creation_date=fecha
            )
            
            team.save()
            return redirect('teams_list')
        
        else:
            return render(request, 'create_team.html', {'form': form})
            
    
    form_team = FormTeam()
    
    return render(request, 'create_team.html', {'form': form_team})


class TeamsList(ListView):
    model=Team
    template_name = 'teams_list.html'

    def get_queryset(self):
        team_name = self.request.GET.get('team_name', '')
        if team_name:
            object_list = self.model.objects.filter(team_name__icontains=team_name)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TeamSearch()
        return context

# def teams_list(request):
    
#     search_name = request.GET.get('team_name')
    
#     if search_name:
#         teams_list = Team.objects.filter(team_name__icontains=search_name) 
#     else:
#         teams_list = Team.objects.all()
    
#     form = TeamSearch()
#     return render(request, 'teams_list.html', {'teams_list': teams_list, 'form': form})


@login_required
def edit_team(request, id):
    team = Team.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormTeam(request.POST)
        if form.is_valid():
            team.team_name = form.cleaned_data.get('team_name')
            team.principal_player = form.cleaned_data.get('principal_player')
            team.creation_date = form.cleaned_data.get('creation_date')
            team.description = form.cleaned_data.get('description')
            team.save()
    
            return redirect('teams_list')
        
        else:
            return render(request, 'edit_team.html', {'form': form, 'team': team})
            
    form_team = FormTeam(initial={
        'team_name': team.team_name, 
        'principal_player': team.principal_player, 
        'creation_date': team.creation_date
    })
    
    return render(request, 'edit_team.html', {'form': form_team, 'team': team})


class DeleteTeam(LoginRequiredMixin, DeleteView):
    model=Team
    template_name = 'delete_team.html'
    success_url = '/teams/'


def show_team(request, id):
    team = Team.objects.get(id=id)
    return render(request, 'show_team.html', {'team': team})


def about_me(request):
    return render(request, 'about_me.html')