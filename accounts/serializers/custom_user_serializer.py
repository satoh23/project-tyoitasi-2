from rest_framework import serializers

from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """ 登録時に使う """
    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = CustomUser(username=validated_data['username'],
                          email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
