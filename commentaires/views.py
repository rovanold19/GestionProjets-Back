from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Commentaire

from .serializers import CommentaireSerializer
from .permissions import EstTacheMembreProjet
from notifications.services import creer_notification

# LIST + CREATE COMMENTAIRES
class ListerCreerCommentaireView(generics.ListCreateAPIView):

    serializer_class = CommentaireSerializer
    permission_classes = [IsAuthenticated, EstTacheMembreProjet] 

    def get_queryset(self):

        id_tache = self.kwargs.get('id_tache')

        return Commentaire.objects.filter(tache_id = id_tache).order_by('-date_creation')

    def perform_create(self, serializer):

        commentaire = serializer.save(auteur=self.request.user)

        tache = commentaire.tache

        if tache.assignation:

            creer_notification(
                destinataire=tache.assignation,
                titre='Nouveau commentaire',
                message=f'Nouveau commentaire sur : {tache.titre}',
                type_notification='NOUVEAU_COMMENTAIRE'
            )

# MODIFIER + SUPPRIMER COMMENTAIRES
class DetailCommentaireView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CommentaireSerializer
    permission_classes = [IsAuthenticated]
    queryset = Commentaire.objects.all()