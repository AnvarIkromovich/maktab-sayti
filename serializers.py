from rest_framework.serializers import ModelSerializer

from schoolsite220.models import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


