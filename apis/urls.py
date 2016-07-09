from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken import views
from apis.views import UserViewSet, ReviewViewSet, sign_up

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'all_reviews', ReviewViewSet)

urlpatterns = [
    url(r'^auth/', views.obtain_auth_token),
    url(r'^sign_up/$', sign_up)
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

urlpatterns += router.urls

