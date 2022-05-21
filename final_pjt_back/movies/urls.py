from django.urls import path
from . import views

# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="movies REST API",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/review/', views.review_create),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_delete),
    path('<int:movie_pk>/movie_like/', views.movie_like),
    path('<int:review_pk>/review_like/', views.review_like),

    path('swagger/', schema_view.with_ui('swagger')),
]