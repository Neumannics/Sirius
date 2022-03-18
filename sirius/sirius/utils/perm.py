from signal import raise_signal
from authorization.models import Permission, Membership
from django.http import HttpResponseForbidden

def hasPerm(action, relation, user, team):
    if user.is_superuser:
        return True
    permission = Permission.objects.get(action=action, relation=relation).pk
    if not permission:
        return False
    user_permissions = Membership.objects.get(user_id=user, team_id=team).role_id.permissions.strip(',').split(',')
    if str(permission) in user_permissions:
        return True
    return False