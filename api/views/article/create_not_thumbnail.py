from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from article.serializers import CreateDetailNotThumbnailSerializer
from article.models import Detail


class CreateNotThumbnailView(generics.CreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = CreateDetailNotThumbnailSerializer
    permission_classes = (IsAuthenticated,)
