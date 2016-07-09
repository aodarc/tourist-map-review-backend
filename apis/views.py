# from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import views
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django_facebook.api import FacebookUserConverter
from open_facebook import OpenFacebook
from apis.serializers import UserSerializer, ReviewObjectSerializer
from apis.models import ReviewObject, UserProfile


# Create your views here.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    # queryset = FacebookCustomUser.objects.all()
    serializer_class = UserSerializer


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReviewObject.objects.all()
    serializer_class = ReviewObjectSerializer

@permission_classes(permissions.BasePermission)
@api_view(['POST',])
def sign_up(request):
    facebook = OpenFacebook(request.data['access_token'])
    if facebook.is_authenticated():
        fb = FacebookUserConverter(facebook)
        # print(facebook.get('me'))
        # print(facebook.get('me/friends'))
        print(fb.get_friends())
        print(fb.facebook_profile_data())
        return Response(facebook.get('me'))