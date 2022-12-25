from rest_framework.serializers import HyperlinkedModelSerializer
from customusers.models import CustomUsers

class CustomUsersModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUsers
        fields = ('username', 'first_name', 'last_name', 'email')
