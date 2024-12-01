from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_csrf_token/', get_csrf_token , name='get_csrf_token'),
    path('login/' , login  , name="login"),
    path('logout/' , logout , name='logout')
]
