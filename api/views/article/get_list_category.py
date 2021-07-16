from rest_framework.permissions import AllowAny
from rest_framework import generics
from article.serializers import ListCategorySerializer
from article.models import Category


class ListCategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer
    permission_classes = (AllowAny,)
