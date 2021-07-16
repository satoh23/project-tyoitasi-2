from rest_framework.permissions import AllowAny
from rest_framework import generics
from article.serializers import DetailArticleSerializer
from article.models import Detail


class GetDetailArticleView(generics.RetrieveAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailArticleSerializer
    permission_classes = (AllowAny,)
