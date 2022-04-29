from urllib.request import urlopen

from team.models import Team
from .perm import get_perms



def get_console_data(team_id, user):
    parents = []
    team = Team.objects.get(pk=team_id)
    parent_id = team.parent_id.pk if team.parent_id else None
    while parent_id != None:
        parent = Team.objects.values('name', 'pk', 'parent_id__pk').get(pk=parent_id)
        parents.append(parent)
        parent_id = parent['parent_id__pk']
    return {
        'team': team, 
        'parents': parents, 
        'perms': get_perms(user, team_id),
    }
