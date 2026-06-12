from .models import Notification


def creer_notification(destinataire, titre, message, type_notification):

    Notification.objects.create(destinataire = destinataire, titre = titre, message = message, type=type_notification)