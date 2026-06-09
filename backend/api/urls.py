from django.urls import path

from api import views

urlpatterns = [
    path("health/", views.health, name="health"),
    path("stats/", views.site_stats, name="site-stats"),
    path("exchange-rate/", views.exchange_rate, name="exchange-rate"),
    path("donations/", views.donations, name="donations"),
    path("receipts/", views.receipts, name="receipts"),
    path("charities/", views.charities, name="charities"),
]
