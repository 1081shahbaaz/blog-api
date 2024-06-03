from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsCommenterOrReadOnly(BasePermission):
    """
    The request is authenticated as a commenter, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user == view.get_object().commenter
        )
        
class IsAuthorOrReadOnly(BasePermission):
    """
    The request is authenticated as a author, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user == view.get_object().author
        )
