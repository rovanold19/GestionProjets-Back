from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Projet(models.Model):

    CHOIX_STATUTS = [
        ('PROGRAMMATION', 'Programmation'),
        ('ACTIF', 'Actif'),
        ('EN_ATTENTE', 'En attente'),
        ('COMPLETE', 'Complete'),
        ('ANNULE', 'Annule'),
    ]

    CHOIX_PRIORITES = [
        ('FAIBLE', 'Faible'),
        ('MOYEN', 'Moyen'),
        ('ELEVE', 'Eleve'),
        ('URGENT', 'Urgent'),
    ]

    titre = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    statut = models.CharField(max_length=20, choices=CHOIX_STATUTS, default='PROGRAMMATION')

    priorite = models.CharField(max_length=20, choices=CHOIX_PRIORITES, default='MOYEN')

    progression = models.PositiveIntegerField(default=0)

    date_debut = models.DateField(null=True, blank=True)

    date_fin = models.DateField(null=True, blank=True)

    proprietaire = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='proprietaire_projet')

    date_creation = models.DateTimeField(auto_now_add=True)

    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre



class MembreProjet(models.Model):

    CHOIX_ROLES = [
        ('ADMINISTRATEUR', 'Administrateur'),
        ('CHEF_PROJET', 'Chef Projet'),
        ('MEMBRE', 'Membre'),
    ]

    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='membres')

    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='membres_projet')

    role = models.CharField(max_length=20, choices=CHOIX_ROLES, default='MEMBRE')

    date_adhesion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['projet', 'utilisateur']

    def __str__(self):
        return f"{self.utilisateur.email} - {self.projet.titre}"