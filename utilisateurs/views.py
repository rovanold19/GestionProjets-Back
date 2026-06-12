from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import *
# Create your views here.

#Recuperer l'utilisateur connecte
class MeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
#Modifier le profil de l'utilisateur
class ModificationProfilView(generics.UpdateAPIView):
    serializer_class = ModificationProfilSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
#Lister tous les utilisateurs
class ListeUtilisateursView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
#Recuperer un utlisateur
class DetailUtilisateurView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class InscriptionView(
    generics.CreateAPIView
):

    serializer_class = (
        InscriptionSerializer
    )

    permission_classes = []