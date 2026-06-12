from django.db import models
from django.conf import settings

from taches.models import Tache


class Commentaire(models.Model):

    tache = models.ForeignKey(Tache, on_delete=models.CASCADE, related_name='commentaires')

    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commentaires')

    contenu = models.TextField()

    date_creation = models.DateTimeField(auto_now_add=True)

    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.auteur.email} - {self.tache.titre}"