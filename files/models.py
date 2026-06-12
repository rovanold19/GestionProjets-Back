from django.db import models
from django.conf import settings

from taches.models import Tache


class Piece_Jointe(models.Model):

    tache = models.ForeignKey(Tache, on_delete=models.CASCADE, related_name='pieces_jointes')

    televerse_par = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pieces_jointes')

    fichier = models.FileField(upload_to='pieces_jointes/')

    nom_fichier = models.CharField(max_length=255)

    date_televersement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_fichier