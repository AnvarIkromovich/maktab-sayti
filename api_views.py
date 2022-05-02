from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from schoolsite220.models import News
from schoolsite220.serializers import NewsSerializer


class NewsViewset(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
