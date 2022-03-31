from backend.models import User
from rest_framework import authentication, exceptions
from rest_framework_simplejwt.state import token_backend
from django.utils import timezone
from django.utils.translation import gettext as _

# Middleware to handle firebase authentication's IdToken


class CustomJWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            if not request.META.get('HTTP_AUTHORIZATION', None):
                return None
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            data = {'token': token}

            valid_data = token_backend.decode(token, verify=True)
            user = User.objects.get(id=valid_data['user_id'])
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])
            return (user, None)  # authentication successful
        except Exception:
            raise exceptions.AuthenticationFailed({
                'detail': _('Invalid or missing token in header')
            }, code=401)

    def authenticate_header(self, request):
        return 'Bearer realm="Access to the site api"[, charset="UTF-8"]'
