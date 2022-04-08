from team.models import Team
from .perm import getPerms

def get_console_data(team_id, user):
    parents = []
    team = Team.objects.get(pk=team_id)
    temp = team.parent_id
    while temp != None:
        parents.append(Team.objects.values('name', 'pk').get(pk=temp))
        temp = temp.parent_id
    return {'team': team, 'parents': parents, 'perms': getPerms(user, team_id)}
    