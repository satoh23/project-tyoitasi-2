from rest_framework.permissions import AllowAny
from rest_framework import generics
from article.serializers import ListDetailSerializer
from article.models import Detail


class ListDetailView(generics.ListAPIView):
    queryset = Detail.objects.all()
    serializer_class = ListDetailSerializer
    permission_classes = (AllowAny,)
    search_fields = ['main_material', ]
