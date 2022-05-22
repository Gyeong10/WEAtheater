from django.urls import path, include
from . import views

# swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_url_patterns = [
    path('api/v1/movies/', include('movies.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="movies REST API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=schema_url_patterns,
)


urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.review_create),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete),
    path('<int:movie_pk>/movie_like/', views.movie_like),
    path('<int:review_pk>/review_like/', views.review_like),
    path('search/<str:input>/', views.search),

    path('swagger/', schema_view.with_ui('swagger')),
]