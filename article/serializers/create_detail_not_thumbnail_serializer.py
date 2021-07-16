from rest_framework import serializers
from article.models import Detail


class CreateDetailNotThumbnailSerializer(serializers.ModelSerializer):
    """記事の作成、編集でサムネイルが存在しない場合に使う(これを使わないとBadRequestになる)"""

    class Meta:
        model = Detail
        fields = ('title', 'body', 'material', 'category', 'author_id')
