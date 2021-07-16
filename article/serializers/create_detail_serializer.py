from rest_framework import serializers
from article.models import Detail
from decouple import config


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class CreateDetailSerializer(serializers.ModelSerializer):
    """記事の作成に使う"""

    thumbnail = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Detail
        fields = ('thumbnail', 'encoded_thumbnail', 'title', 'body', 'material', 'category', 'author_id')

    def create(self, validated_data):
        article = Detail(thumbnail=validated_data['thumbnail'],
                         encoded_thumbnail=validated_data['encoded_thumbnail'],
                         title=validated_data['title'],
                         body=validated_data['body'],
                         material=validated_data['material'],
                         category=validated_data['category'],
                         author_id=validated_data['author_id'],
                         )
        article.save()
        return article
