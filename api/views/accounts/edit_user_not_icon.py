from accounts.serializers import EditUserNotIconSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from accounts.models.custom_user import CustomUser


class EditUserNotIconView(RetrieveUpdateAPIView):
    """
    cookieにAccessTokenが入っている時だけアクセス可能
    """
    serializer_class = EditUserNotIconSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """
        django-rest-swaggerが呼び出される場合に使う
        """
        return get_user_model().objects.none()

    def patch(self, request, *args, **kwargs):
        try:
            user_id = request.data['user_id']
            if user_id:
                user = CustomUser.objects.get(pk=user_id)
                user.user_icon.delete()
        except KeyError:
            pass
        return self.partial_update(request, *args, **kwargs)

