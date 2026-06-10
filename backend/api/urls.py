from django.urls import path
from django.views.decorators.cache import cache_page

from api import views

PUBLIC_READ_CACHE_SECONDS = 60

urlpatterns = [
    path("health/", views.health, name="health"),
    path("receipts/", views.receipts, name="receipts"),
    path(
        "stats/",
        cache_page(PUBLIC_READ_CACHE_SECONDS)(views.site_stats),
        name="site-stats",
    ),
    path(
        "exchange-rate/",
        cache_page(PUBLIC_READ_CACHE_SECONDS)(views.exchange_rate),
        name="exchange-rate",
    ),
    path(
        "donations/",
        cache_page(PUBLIC_READ_CACHE_SECONDS)(views.donations),
        name="donations",
    ),
    path(
        "charities/",
        cache_page(PUBLIC_READ_CACHE_SECONDS)(views.charities),
        name="charities",
    ),
]
