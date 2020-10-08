from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet, UserLoginApiview, ProfileViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('feed', ProfileViewSet)

urlpatterns = [
    path('login/', UserLoginApiview.as_view(), name='login'),
    path('', include(router.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
