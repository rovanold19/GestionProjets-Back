from rest_framework.permissions import BasePermission
from projets.models import MembreProjet
from taches.models import Tache

class EstTacheMembreProjet(BasePermission):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        
        id_tache = view.kwargs.get('id_tache')  
        if not id_tache:
            id_tache = request.data.get('tache')  

        if not id_tache:
            return True

        try:
            tache = Tache.objects.get(pk=id_tache)

            if tache.projet.proprietaire == request.user:
                return True

            
            return MembreProjet.objects.filter(
                projet=tache.projet, 
                utilisateur=request.user
            ).exists()

        except Tache.DoesNotExist:
            return False
