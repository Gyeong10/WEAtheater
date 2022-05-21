from django.urls import path, include
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_url_patterns = [
    path('api/v1/accounts/', include('accounts.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="accounts REST API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=schema_url_patterns,
)


urlpatterns = [
    path('profile/<username>/', views.profile),

    path('swagger/', schema_view.with_ui('swagger')),
]
