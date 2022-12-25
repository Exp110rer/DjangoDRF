from rest_framework.serializers import HyperlinkedModelSerializer
from authors.models import Authors

class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'
