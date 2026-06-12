from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from projets.models import Projet


class Tache(models.Model):

    CHOIX_STATUT = [
        ('A_FAIRE', 'A faire'),
        ('EN_COURS', 'En cours'),
        ('En_REVISION', 'En revision'),
        ('TERMINE', 'Termine'),
    ]

    CHOIX_PRIORITE = [
        ('BAS', 'Bas'),
        ('MOYEN', 'Moyen'),
        ('ELEVE', 'Eleve'),
        ('URGENT', 'Urgent'),
    ]

    titre = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    statut = models.CharField(max_length=20, choices=CHOIX_STATUT, default='A_FAIRE')

    priorite = models.CharField(max_length=20, choices=CHOIX_PRIORITE, default='MOYEN')

    progression = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])

    date_fermeture = models.DateField(null=True, blank=True)

    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='taches')

    assignation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='taches_assignees')

    createur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='taches_crees')

    date_creation = models.DateTimeField(auto_now_add=True)

    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre