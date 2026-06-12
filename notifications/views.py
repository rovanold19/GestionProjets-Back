from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer


# LISTE NOTIFICATIONS
class ListeNotificationView(generics.ListAPIView):

    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Notification.objects.filter(destinataire = self.request.user).order_by('-date_creation')

# MARQUER COMME LUE
class MarquerNotificationCommeLueView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        notification = Notification.objects.get(pk=pk,destinataire = request.user)

        notification.est_lue = True

        notification.save()

        return Response({'message': 'Notification marquee comme lue'})
    
    
