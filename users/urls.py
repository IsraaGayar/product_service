from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import MyTokenObtainPairView, UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='users')

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]