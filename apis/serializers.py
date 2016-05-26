from django.contrib.auth.models import User
from rest_framework import serializers
from apis.models import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ReviewObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewObject
        fields = ('lat', 'lon', 'title', 'text', 'description', 'title_image')
