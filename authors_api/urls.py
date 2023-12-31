from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from dj_rest_auth.views import PasswordResetConfirmView
from core_apps.users.views import CustomUserDetailsView


schema_view = get_schema_view(
    openapi.Info(
        title="redi API",
        default_version="v1",
        description="API Endpoints",
        contact=openapi.Contact(email="hredi1994@gmail.com"),
        license=openapi.License(name="MIT License",),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/user/", CustomUserDetailsView.as_view(),
         name="user_details"),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/auth/password/reset/confirm/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("api/v1/profiles/", include("core_apps.profiles.urls"))
]

admin.site.site_header = "Redi Admin API"

admin.site.site_tile = "Redi API Admin Panel"

admin.site.index_tile = "Welcome to Redi's API"