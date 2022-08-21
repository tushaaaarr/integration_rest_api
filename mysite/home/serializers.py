from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TestModel
class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class TestApi_data(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestModel
        fields = ('title','description')

