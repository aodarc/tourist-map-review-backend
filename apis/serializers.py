# from django.contrib.auth.models import User
from django_facebook.models import FacebookUser
from rest_framework import serializers
from apis.models import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FacebookUser
        fields = ('user_id', 'facebook_id', 'name')


class ReviewObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewObject
        fields = ('lat', 'lon', 'title', 'text', 'description', 'title_image')
