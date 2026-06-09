from rest_framework.throttling import AnonRateThrottle


class WriteRateThrottle(AnonRateThrottle):
    """Rate-limit only unsafe (write) requests by client IP.

    The public write endpoints (receipt upload, donation report) are
    unauthenticated, so without a limit an anonymous client could spam uploads.

    Reads (GET/HEAD) are cheap and may legitimately arrive in volume
    from users behind a shared IP, so they are not throttled.
    """

    def allow_request(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return super().allow_request(request, view)


class ReceiptUploadThrottle(WriteRateThrottle):
    scope = "receipts"


class DonationReportThrottle(WriteRateThrottle):
    scope = "donations"
