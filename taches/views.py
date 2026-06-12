from django.db.models import Q
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from .models import Tache
from .serializers import (TacheSerializer, CreerTacheSerializer)
from .permissions import EstMembreProjet
from notifications.services import creer_notification



# LIST + CREATE TASK
class ListeTachesCreateView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated, EstMembreProjet]

    filter_backends = [filters.SearchFilter]

    search_fields = ['titre', 'description', 'statut', 'priorite']

    def get_queryset(self):
        user = self.request.user
        
        # On filtre les tâches dont le projet a pour propriétaire l'utilisateur connecté,
        # OU les tâches dont le projet compte l'utilisateur connecté parmi ses membres.
        return Tache.objects.filter(
            Q(projet__proprietaire=user) | 
            Q(projet__membres__utilisateur=user)
        ).distinct().order_by('-id')


    def get_serializer_class(self):

        if self.request.method == 'POST':
            return CreerTacheSerializer

        return TacheSerializer

    def perform_create(self, serializer):
    
        tache = serializer.save(createur=self.request.user)

        if tache.assignation:

            creer_notification(
                destinataire=tache.assignation,
                titre='Nouvelle tâche assignée',
                message=f'Vous avez été assigné à la tâche : {tache.titre}',
                type_notification='TACHE_ASSIGNEE'
            )


# DETAIL TASK
class DetailTacheView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Tache.objects.all()

    def get_serializer_class(self):

        if self.request.method in ['PUT', 'PATCH']:
            return CreerTacheSerializer

        return TacheSerializer