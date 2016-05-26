from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from apis.views import UserViewSet, ReviewViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'all_reviews', ReviewViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

