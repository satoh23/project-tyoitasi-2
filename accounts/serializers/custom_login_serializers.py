from dj_rest_auth.serializers import LoginSerializer


class CustomLoginSerializer(LoginSerializer):
    """ログイン時のフォームからユーザー名を消す"""
    username = None
