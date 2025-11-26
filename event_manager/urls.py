from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, LoginView, EventViewSet, ExperienceViewSet


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'experiences', views.ExperienceViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]