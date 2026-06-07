from pathlib import Path

from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import FileResponse, Http404, HttpResponse
from django.views.decorators.http import require_GET


@staff_member_required
@require_GET
def protected_media(request, path):
    """Serve a file from PRIVATE_MEDIA_ROOT to staff only.

    Private uploads (donation receipts) are considered sensitive and are never public.
    They live under their own root, separate from the public MEDIA_ROOT, and are only
    reachable through this view.
    """
    private_root = Path(settings.PRIVATE_MEDIA_ROOT).resolve()
    full_path = (private_root / path).resolve()
    if private_root not in full_path.parents or not full_path.is_file():
        raise Http404
    return FileResponse(open(full_path, "rb"))


@require_GET
def spa_index(request):
    """Serve the built SPA's index.html"""
    index_file = settings.SPA_DIR / "index.html"
    if index_file.exists():
        return FileResponse(open(index_file, "rb"))
    return HttpResponse(
        "SPA build not found. Run `npm run build` in frontend/ "
        "(or use the Vite dev server during development).",
        status=501,
        content_type="text/plain",
    )
