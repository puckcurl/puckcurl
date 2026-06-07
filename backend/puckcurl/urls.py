from django.contrib import admin
from django.urls import include, path, re_path

from puckcurl.views import protected_media, spa_index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    # Staff-only private media (receipts). Must precede the SPA catch-all below.
    re_path(r"^private/(?P<path>.+)$", protected_media, name="protected-media"),
    # Catch-all for the SPA. Frontend handles routing for child routes.
    re_path(r"^.*$", spa_index, name="spa"),
]
