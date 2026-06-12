from django.urls import path

from .views import (
    ListerCreerProjetView, DetailProjetView, AjouterMembreView, EnleverMembreView, ListeMembresProjetView)

urlpatterns = [
    path('',ListerCreerProjetView.as_view()),

    path('<int:pk>/', DetailProjetView.as_view()),

    path('<int:pk>/ajouter-membre/', AjouterMembreView.as_view()),

    path('<int:pk>/enlever-membre/<int:id_user>/', EnleverMembreView.as_view()),

    path('<int:pk>/membres/',ListeMembresProjetView.as_view()),
]