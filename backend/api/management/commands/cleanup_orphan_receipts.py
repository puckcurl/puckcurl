from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from api.models import DonationReceipt

ORPHAN_AGE = timedelta(minutes=30)
RETENTION_AGE = timedelta(days=365)


class Command(BaseCommand):
    help = (
        "Cleans up donation receipts. Deletes receipts older than 30 minutes "
        "that no donation ever claimed (abandoned uploads). Deletes every "
        "receipt older than one year regardless of state (retention)."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Report what would be deleted without deleting anything.",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]
        now = timezone.now()
        orphan_cutoff = now - ORPHAN_AGE
        retention_cutoff = now - RETENTION_AGE

        # Everything older than a year, attached or not (retention).
        expired = DonationReceipt.objects.filter(created__lt=retention_cutoff)  # ty: ignore[unresolved-attribute]

        # Unclaimed uploads in the 30-minutes-to-1-year window.
        orphans = DonationReceipt.objects.filter(  # ty: ignore[unresolved-attribute]
            created__lt=orphan_cutoff,
            created__gte=retention_cutoff,
            donation__isnull=True,
        )

        expired_count = expired.count()
        orphan_count = orphans.count()

        if dry_run:
            self.stdout.write(
                f"[dry-run] would delete {orphan_count} orphaned receipt(s) "
                f"and {expired_count} expired receipt(s)."
            )
            return

        orphans.delete()
        expired.delete()
        self.stdout.write(
            self.style.SUCCESS(
                f"Deleted {orphan_count} orphaned receipt(s) and "
                f"{expired_count} expired receipt(s)."
            )
        )
