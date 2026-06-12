from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Piece_Jointe
from .serializers import PiecesJointesSerializer
from .permissions import EstTacheMembre


# LISTER + CREER PIECES JOINTES
class ListerCreerPiecesJointesView(generics.ListCreateAPIView):

    serializer_class = PiecesJointesSerializer

    permission_classes = [IsAuthenticated, EstTacheMembre]

    def get_queryset(self):

        tache_id = self.kwargs.get('tache_id')

        return Piece_Jointe.objects.filter(
            tache_id = tache_id).order_by('-id')

    def perform_create(self, serializer):

        fichier_televerse = self.request.FILES.get('fichier')
        nom = fichier_televerse.name if fichier_televerse else "fichier_anonyme"
        serializer.save(televerse_par=self.request.user, nom_fichier=nom)


# DELETE ATTACHMENT
class SupprimerPieceJointeView(generics.DestroyAPIView):

    queryset = Piece_Jointe.objects.all()

    serializer_class = PiecesJointesSerializer

    permission_classes = [IsAuthenticated]