from django.db.models import Q
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utilisateurs.models import User
from .models import (Projet,MembreProjet)
from .serializers import (ProjetSerializer, AjoutMembreSerializer)
from .permissions import EstProprietaireProjet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Projet
from .serializers import MembreProjetSerializer


# LISTER + CREER
class ListerCreerProjetView(generics.ListCreateAPIView):

    serializer_class = ProjetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['titre', 'description', 'statut', 'priorite']

    def get_queryset(self):
        user = self.request.user

        return Projet.objects.filter(Q(proprietaire=user) | Q(membres__utilisateur=user)).distinct().order_by('-id')

    def perform_create(self, serializer):

        projet = serializer.save(proprietaire = self.request.user)

        projet = serializer.save(proprietaire=self.request.user)

        MembreProjet.objects.create(
            projet=projet, 
            utilisateur=self.request.user,  
            role='ADMINISTRATEUR'
        )


# DETAILLER + MODIFIER + SUPPRESSION
class DetailProjetView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProjetSerializer
    permission_classes = [IsAuthenticated, EstProprietaireProjet]
    queryset = Projet.objects.all()

# AJOUTER MEMEBRE
class AjouterMembreView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        projet = Projet.objects.get(pk=pk)

        if projet.proprietaire != request.user:

            return Response(
                {
                    'error': 'Pas Autorise'
                },
                status=403
            )

        serializer = AjoutMembreSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = User.objects.get(pk=serializer.validated_data['id_user'])

        membre, cree = MembreProjet.objects.get_or_create(projet=projet, utilisateur=user,
            defaults={
                'role': serializer.validated_data['role']
            }
        )

        if not cree:

            return Response(
                {
                    'message': "L'utilisateur est deja membre"
                },
                status=400
            )

        return Response(
            {
                'message': 'Membre ajoute avec succes'
            }
        )


# Enlever Membre
class EnleverMembreView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, id_user):

        projet = Projet.objects.get(pk=pk)

        if projet.proprietaire != request.user:

            return Response(
                {
                    'error': 'Pas Autorise'
                },
                status=403
            )

        MembreProjet.objects.filter(projet=projet,utilisateur_id=id_user).delete()

        return Response(
            {
                'message': 'Member retire'
            }
        )


class ListeMembresProjetView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        projet = Projet.objects.get(pk=pk)

        serializer = MembreProjetSerializer(
            projet.membres.all(),
            many=True
        )

        return Response(serializer.data)