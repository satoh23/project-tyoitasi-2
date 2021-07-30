from rest_framework.permissions import AllowAny
from rest_framework import generics
from django_filters import rest_framework as filters
from article.serializers import ListDetailSerializer
from article.models import Detail


class ArticleFilter(filters.FilterSet):
    main_material = filters.CharFilter(
        name="main_material", lookup_expr='contains')

    class Meta:
        model = Detail
        fields = ['main_material', ]


class ListDetailView(generics.ListAPIView):
    queryset = Detail.objects.all()
    serializer_class = ListDetailSerializer
    permission_classes = (AllowAny,)
    filter_class = ArticleFilter
