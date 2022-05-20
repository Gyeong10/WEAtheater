from django.urls import path
from . import views


urlpatterns = [
    path('/', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/review/', views.review_create),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_delete),
    path('<int:movie_pk>/like/', views.movie_like),
    path('<int:review_pk>/like/', views.review_like),
]