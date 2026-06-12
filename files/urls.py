from django.urls import path
from .views import ListerCreerPiecesJointesView, SupprimerPieceJointeView


urlpatterns = [

    path('tache/<int:tache_id>/', ListerCreerPiecesJointesView.as_view()),

    path('<int:pk>/', SupprimerPieceJointeView.as_view()),
]