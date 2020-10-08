
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import serializers
from .models import UserProfile, Profile
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile, UpdateProfileStatus
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.parsers import FormParser, MultiPartParser


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


"""
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
"""


class UserLoginApiview(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    """
        def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    """


class ProfileViewSet(viewsets.ModelViewSet):
    parser_classes = (FormParser, MultiPartParser)
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (
        UpdateProfileStatus,
        IsAuthenticatedOrReadOnly,
    )

    def profile_create(self, serializer):
        serializer.save(user_profile=self.request.user)
