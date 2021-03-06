from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    """Allow ReadOnly permissions if the request is a safe method"""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CanEditProperty(BasePermission):
    """Client admins should be able to edit property they own"""

    def has_object_permission(self, request, view, obj):

        user = request.user
        if request.method in SAFE_METHODS:
            return True
        if user.is_authenticated and user.role == 'CA':
            return user == obj.client.client_admin
        if user.is_authenticated and user.role == 'LA':
            return True
        return False


class IsClientAdmin(BasePermission):
    """Grants client admins full access"""

    def has_permission(self, request, view):
        user = request.user if request.user.is_authenticated else None
        if user:
            client = user.employer.first()
            return client and user.role == 'CA' and \
                client.approval_status == 'approved'


class IsBuyer(BasePermission):
    """ Check if user is buyer then grants access."""

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return (
                request.user.role == 'LA' or request.user.role == 'BY'
                or request.user.role == 'CA')
        return request.user.role == 'BY'


class IsOwner(BasePermission):
    """ a user can be able to edit a property enquiry belonging to only him """

    def has_object_permission(self, request, view, obj):

        user = request.user

        if request.method in SAFE_METHODS:
            return True

        return obj.requester == user


class IsReviewer(BasePermission):
    """ check if its the reviewer then allow to update, delete"""

    def has_object_permission(self, request, view, obj):

        user = request.user

        if request.method in SAFE_METHODS:
            return True
        return obj.reviewer == user


class IsBuyerOrReadOnly(BasePermission):
    """ Check if user is buyer and logged in then grants access."""

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'BY'
        )

class IsAdmin(BasePermission):
    """ check if its the Admin then allow to delete"""

    def has_object_permission(self, request, view, obj):

        user = request.user

        if request.method == 'DELETE' and user.role == 'LA':
            return True
