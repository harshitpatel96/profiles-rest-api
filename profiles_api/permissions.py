from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            # Safe methods is GET
            return True

        # if not a safe method then we will only allow it if object user id == request user id
        return obj.id == request.user.id
