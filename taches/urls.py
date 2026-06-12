from django.urls import path

from .views import (ListeTachesCreateView, DetailTacheView,)

urlpatterns = [

    path('',ListeTachesCreateView.as_view()),

    path('<int:pk>/',DetailTacheView.as_view()),
]