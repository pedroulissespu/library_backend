from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.contrib import admin
from django.urls import path, include

from library.users.api.views import UserCreate

API_PREFIX = "api/v1/"

urlpatterns = [
    path(f"{API_PREFIX}", include("config.api_router"), name="api-root"),
    path(f"admin/", admin.site.urls),
    path(f"{API_PREFIX}users/", UserCreate.as_view(), name="user_create"),
    path(f"{API_PREFIX}books/", include("library.books.api.urls")),
    path(f"{API_PREFIX}authors/", include("library.authors.api.urls")),
    path(f"{API_PREFIX}borrow/", include("library.borrow.api.urls")),
    path(f"{API_PREFIX}auth/", include("rest_framework.urls")),
    path(
        f"{API_PREFIX}token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        f"{API_PREFIX}token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path(f"{API_PREFIX}token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(f"{API_PREFIX}schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        f"{API_PREFIX}docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]
