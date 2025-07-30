from rest_framework_simplejwt.views import TokenObtainPairView

from appUsers.serializers import CustomTokenObtainPairSerializer


class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
