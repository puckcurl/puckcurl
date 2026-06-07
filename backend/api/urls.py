from django.urls import path

from api import views

urlpatterns = [
    path("health/", views.health, name="health"),
    path("stats/", views.site_stats, name="site-stats"),
]
