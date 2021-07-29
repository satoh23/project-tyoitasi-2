from rest_framework import serializers

from accounts.models import CustomUser


class EditUserNotIconSerializer(serializers.ModelSerializer):
    """ アイコン以外の編集時に使う """

    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'email', 'password', 'user_profile',)
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        read_only_fields = ('id', 'email',)

