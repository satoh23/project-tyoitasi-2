from rest_framework import serializers
from article.models import Detail

from rest_framework.serializers import SerializerMethodField


class ListDetailSerializer(serializers.ModelSerializer):
    author = SerializerMethodField()
    category_name = SerializerMethodField()

    class Meta:
        model = Detail
        fields = ('id', 'thumbnail', 'title', 'body', 'material', 'category_name', 'category', 'created_date', 'author', 'author_id')

    def get_author(self, obj):
        try:
            author_name = obj.author_id.username
            return author_name
        except:
            return None

    def get_category_name(self, obj):
        try:
            category_name = obj.category.category
            return category_name
        except:
            return None