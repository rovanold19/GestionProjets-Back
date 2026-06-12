from django.urls import path
from .views import  ListeNotificationView, MarquerNotificationCommeLueView


urlpatterns = [
    path('', ListeNotificationView.as_view()),

    path('<int:pk>/lue/', MarquerNotificationCommeLueView.as_view()),
]