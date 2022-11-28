from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from social_auth_app.views import UserProfile_ViewSet, Post_ViewSet

router = routers.DefaultRouter()

router.register(r'profile', UserProfile_ViewSet, basename='profile')
router.register(r'post', Post_ViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('social_auth_app.urls')),
    path('user/', include('user_auth.urls')),
    path('admin/', admin.site.urls),
]
