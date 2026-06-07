from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import Donation, SiteStats
from api.serializers import SiteStatsSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def health(request: Request) -> Response:
    """Basic liveness probe"""
    return Response({"status": "ok"})


@api_view(["GET"])
@permission_classes([AllowAny])
def site_stats(request: Request) -> Response:
    """Public campaign stats"""
    serializer = SiteStatsSerializer(
        {
            "verified_total": Donation.verified_total(),
            "verified_count": Donation.verified_count(),
            "goals_scored": SiteStats.load().goals_scored,
        }
    )
    return Response(serializer.data)
