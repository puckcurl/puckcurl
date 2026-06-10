from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from api.models import Charity


class Command(BaseCommand):
    help = (
        "Deletes charities that are still unapproved "
        "and have no donations attributed to them."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Report what would be deleted without deleting anything.",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]
        cutoff = timezone.now() - timedelta(minutes=30)

        orphans = Charity.objects.filter(  # ty: ignore[unresolved-attribute]
            approved=False,
            donations__isnull=True,
            created__lt=cutoff,
        )
        orphan_count = orphans.count()

        if dry_run:
            self.stdout.write(
                f"[dry-run] would delete {orphan_count} orphaned charit(ies)."
            )
            return

        orphans.delete()
        self.stdout.write(
            self.style.SUCCESS(f"Deleted {orphan_count} orphaned charit(ies).")
        )
