from django.db import models
from django.conf import settings


class Notification(models.Model):

    TYPES_CHOIX = [
        ('TACHE_ASSIGNEE', 'Tache Assignee'),
        ('NOUVEAU_COMMENTAIRE', 'Nouveau Commentaire'),
        ('PROJET_INVITE', 'Projet Invite'),
        ('LIGNE_ROUGE', 'Ligne rouge'),
    ]

    destinataire = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')

    titre = models.CharField(max_length=255)

    message = models.TextField()

    type = models.CharField(max_length=30, choices=TYPES_CHOIX)

    est_lue = models.BooleanField(default=False)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre