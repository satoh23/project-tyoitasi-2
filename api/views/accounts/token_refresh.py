from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.serializers import CookieTokenRefreshSerializer
from django.conf import settings
from django.utils import timezone


def set_jwt_access_cookie(response, access_token):
    from rest_framework_simplejwt.settings import api_settings as jwt_settings
    cookie_name = getattr(settings, 'JWT_AUTH_COOKIE', None)
    access_token_expiration = (timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME)
    cookie_secure = getattr(settings, 'JWT_AUTH_SECURE', False)
    cookie_httponly = getattr(settings, 'JWT_AUTH_HTTPONLY', True)
    cookie_samesite = getattr(settings, 'JWT_AUTH_SAMESITE', 'Lax')

    if cookie_name:
        response.set_cookie(
            cookie_name,
            access_token,
            expires=access_token_expiration,
            secure=cookie_secure,
            httponly=cookie_httponly,
            samesite=cookie_samesite
        )


def set_jwt_refresh_cookie(response, refresh_token):
    from rest_framework_simplejwt.settings import api_settings as jwt_settings
    refresh_token_expiration = (timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME)
    refresh_cookie_name = getattr(settings, 'JWT_AUTH_REFRESH_COOKIE', None)
    refresh_cookie_path = getattr(settings, 'JWT_AUTH_REFRESH_COOKIE_PATH', '/')
    cookie_secure = getattr(settings, 'JWT_AUTH_SECURE', False)
    cookie_httponly = getattr(settings, 'JWT_AUTH_HTTPONLY', True)
    cookie_samesite = getattr(settings, 'JWT_AUTH_SAMESITE', 'Lax')

    if refresh_cookie_name:
        response.set_cookie(
            refresh_cookie_name,
            refresh_token,
            expires=refresh_token_expiration,
            secure=cookie_secure,
            httponly=cookie_httponly,
            samesite=cookie_samesite,
            path=refresh_cookie_path
        )


def get_refresh_view():
    """
    CookieからRefreshTokenを取り出してAccessTokenとRefreshTokenを再発行する
    その後、使用したRefreshTokenをblacklistに追加する
    """

    class RefreshViewWithCookieSupport(TokenRefreshView):
        serializer_class = CookieTokenRefreshSerializer

        def finalize_response(self, request, response, *args, **kwargs):
            if response.status_code == 200 and 'access' in response.data:
                set_jwt_access_cookie(response, response.data['access'])
                response.data['access_token_expiration'] = (timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME)
            if response.status_code == 200 and 'refresh' in response.data:
                set_jwt_refresh_cookie(response, response.data['refresh'])
            return super().finalize_response(request, response, *args, **kwargs)

    return RefreshViewWithCookieSupport
