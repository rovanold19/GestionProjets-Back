from rest_framework import serializers
from taches.models import Tache
from .models import (Projet, MembreProjet)
from taches.serializers import TacheSerializer
from utilisateurs.serializers import UserSerializer

from utilisateurs.models import User


class MembreProjetSerializer(serializers.ModelSerializer):

    utilisateur = UserSerializer(read_only=True)

    class Meta:
        model = MembreProjet
        fields = ['id', 'utilisateur', 'role', 'date_adhesion']


class ProjetSerializer(
    serializers.ModelSerializer
):

    proprietaire = UserSerializer(read_only=True)
    taches = TacheSerializer(many=True,read_only=True)
    membres = MembreProjetSerializer(many=True, read_only=True)

    class Meta:
        model = Projet

        fields = ['id', 'titre','description','progression', 'statut','priorite','taches','date_debut','date_fin','proprietaire','membres','date_creation','date_modification']
def get_progression(self, obj):

    taches = obj.taches.all()

    if not taches.exists():
        return 0

    total = sum(
        tache.progression
        for tache in taches
    )

    return round(
        total / taches.count()
    )


class AjoutMembreSerializer(serializers.Serializer):

    id_user = serializers.IntegerField()

    role = serializers.ChoiceField(
        choices=['ADMINISTRATEUR', 'MEMBRE']
    )

