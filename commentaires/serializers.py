from rest_framework import serializers

from .models import Commentaire

from utilisateurs.serializers import UserSerializer

class CommentaireSerializer(serializers.ModelSerializer):

    auteur = UserSerializer(read_only=True)

    class Meta:
        model = Commentaire
        fields = [
            'id',
            'tache',
            'auteur',
            'contenu',
            'date_creation',
            'date_modification',
        ]