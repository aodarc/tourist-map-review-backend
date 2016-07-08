from django.contrib.auth.models import User
from rest_framework import viewsets
from apis.serializers import UserSerializer, ReviewObjectSerializer
from apis.models import ReviewObject


# Create your views here.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReviewObject.objects.all()
    serializer_class = ReviewObjectSerializer
