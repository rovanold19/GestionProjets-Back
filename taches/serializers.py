from rest_framework import serializers
from .models import Tache
from utilisateurs.serializers import UserSerializer




class TacheSerializer(serializers.ModelSerializer):

    assignation = UserSerializer(read_only=True)

    createur = UserSerializer(read_only=True)

    projet = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Tache

        fields = [
            'id',
            'titre',
            'description',
            'statut',
            'priorite',
            'progression',
            'date_fermeture',
            'projet',
            'assignation',
            'createur',
            'date_creation',
            'date_modification',
        ]


class CreerTacheSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tache

        fields = [
            'titre',
            'description',
            'statut',
            'priorite',
            'progression',
            'date_fermeture',
            'projet',
            'assignation',
        ]