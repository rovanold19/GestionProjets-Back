from rest_framework.permissions import BasePermission
from projets.models import MembreProjet
from taches.models import Tache


class EstTacheMembre(BasePermission):

    def has_permission(self, request, view):

        id_tache = request.data.get('tache')

        if not id_tache:
            return True

        try:

            tache = Tache.objects.get(pk=id_tache)
            return MembreProjet.objects.filter(projet=tache.projet, utilisateur=request.user).exists()

        except Tache.DoesNotExist:

            return False