from rest_framework.permissions import BasePermission
from projets.models import MembreProjet, Projet

class EstMembreProjet(BasePermission):

    def has_permission(self, request, view):
        # 1. Vérification de connexion globale
        if not request.user or not request.user.is_authenticated:
            return False

        # Si c'est une simple lecture de liste (GET), on fait confiance à get_queryset()
        if request.method == 'GET':
            return True

        # 2. Si c'est une création (POST), on analyse le projet cible
        id_projet = request.data.get('projet')
        if not id_projet:
            return True # On laisse le serializer Django lever l'erreur "champ obligatoire"

        try:
            # Vérification A : L'utilisateur est-il le propriétaire/créateur du projet ?
            projet = Projet.objects.get(pk=id_projet)
            if projet.proprietaire == request.user:
                return True
        except Projet.DoesNotExist:
            return False # Projet inconnu, on bloque l'accès

        # Vérification B : L'utilisateur est-il enregistré comme membre ?
        # CORRECTION SYNTAXE : projet_id et utilisateur (conforme à votre modèle MembreProjet)
        return MembreProjet.objects.filter(
            projet_id=id_projet, 
            utilisateur=request.user
        ).exists()
