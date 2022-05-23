from django.urls import path, include
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_url_patterns = [
    path('api/v1/community/', include('community.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="community REST API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=schema_url_patterns,
)


urlpatterns = [
    path('', views.article_list_or_create),
    path('category/<category>/', views.category_article_list),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('<int:article_pk>/like/', views.article_like),
    path('<int:article_pk>/comments/', views.comment_create),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),

    path('swagger/', schema_view.with_ui('swagger')),
]
