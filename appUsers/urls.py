from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from appUsers.views.auth import CustomLoginView
from appUsers.views.register import RegisterView

urlpatterns = [
    path("user/login/", CustomLoginView.as_view(), name="token_obtain_pair"),
    path("user/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/register/", RegisterView.as_view(), name="token_refresh"),
]
