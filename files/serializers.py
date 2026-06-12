from rest_framework import serializers
from .models import Piece_Jointe
from utilisateurs.serializers import UserSerializer


class PiecesJointesSerializer(serializers.ModelSerializer):

    televerse_par = UserSerializer(read_only=True)

    class Meta:
        model = Piece_Jointe

        fields = [
            'id',
            'tache',
            'televerse_par',
            'fichier',
            'nom_fichier',
            'date_televersement',
        ]

        read_only_fields = ['nom_fichier', 'televerse_par']