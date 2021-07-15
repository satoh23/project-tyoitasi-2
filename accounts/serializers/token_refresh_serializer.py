from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from django.conf import settings


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None
    def extract_refresh_token(self):
        request = self.context['request']
        if request.COOKIES['refresh']:
            return request.COOKIES['refresh']
        cookie_name = getattr(settings, 'JWT_AUTH_REFRESH_COOKIE', None)
        if cookie_name and cookie_name in request.COOKIES:
            return request.COOKIES.get(cookie_name)
        else:
            from rest_framework_simplejwt.exceptions import InvalidToken
            raise InvalidToken('No valid refresh token found.')

    def validate(self, attrs):
        attrs['refresh'] = self.extract_refresh_token()
        return super().validate(attrs)
