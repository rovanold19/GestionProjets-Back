from django.urls import path
from .views import ListerCreerCommentaireView, DetailCommentaireView

urlpatterns = [

    path('tache/<int:id_tache>/', ListerCreerCommentaireView.as_view()),

    path('<int:pk>/', DetailCommentaireView.as_view()),
]