from rest_framework.permissions import BasePermission


class EstProprietaireProjet(BasePermission):

    def has_object_permission(
        self,
        request,
        view,
        obj
    ):

        return obj.proprietaire == request.user