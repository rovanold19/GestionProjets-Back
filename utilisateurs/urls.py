from django.urls import path

from .views import *

urlpatterns = [
    path('me/', MeView.as_view()),
    path('me/modifier/', ModificationProfilView.as_view()),
    path('liste/', ListeUtilisateursView.as_view()),
    path('detail/<int:pk>/', DetailUtilisateurView.as_view()),
    path('inscription/',InscriptionView.as_view()),      
]
