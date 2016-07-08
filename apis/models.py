from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
from django_facebook.models import FacebookModel, get_user_model
from django_facebook.utils import get_profile_model


# Create your models here.

class UserProfile(FacebookModel):
    """
    Inherit the properties from django facebook
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)


@receiver(post_save)
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if sender == get_user_model():
        user = instance
        profile_model = get_profile_model()
        if profile_model == UserProfile and created:
            profile, new = UserProfile.objects.get_or_create(user=instance)


class ReviewObject(models.Model):
    lat = models.FloatField(verbose_name='lat', db_index=True, blank=False, null=False, default=49.836085)
    lon = models.FloatField(verbose_name='lon', db_index=True, blank=False, null=False, default=24.005691)
    title = models.CharField(max_length=255, verbose_name=u'Заголовок', db_index=True, unique=True)
    description = models.TextField(max_length=300,
                                   verbose_name=u'Короткий опис',
                                   default='Some Description',
                                   blank=False)
    text = models.TextField(max_length=3000, verbose_name=u'Текст статті')
    title_image = models.ImageField(upload_to='./reviews/images',
                                    verbose_name=u'Головне зоображення',
                                    blank=True,
                                    default='./reviews/images/maps.png')

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
