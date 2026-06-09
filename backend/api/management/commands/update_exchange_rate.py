from decimal import Decimal, InvalidOperation

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from api.models import SiteStats
from libraries.currencylayer.client import CurrencyLayerAPIClient
from libraries.currencylayer.exceptions import CurrencyLayerAPIException

# SiteStats.ca_exchange_rate is Canadian dollars
# per 1 USD, so we always fetch USD to CAD
SOURCE_CURRENCY = "USD"
TARGET_CURRENCY = "CAD"


class Command(BaseCommand):
    help = (
        "Fetches the current USD to CAD exchange rate from CurrencyLayer and "
        "stores it on the SiteStats singleton (ca_exchange_rate)."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Fetch and report the rate without saving it.",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]

        api_key = settings.CURRENCYLAYER_API_KEY
        if not api_key:
            raise CommandError("CURRENCYLAYER_API_KEY is not configured.")

        client = CurrencyLayerAPIClient(api_key=api_key)

        try:
            rates = client.get_rate(
                from_currency=SOURCE_CURRENCY,
                to_currency=TARGET_CURRENCY,
            )
        except CurrencyLayerAPIException as exc:
            raise CommandError(f"Failed to fetch exchange rate: {exc}") from exc

        if TARGET_CURRENCY not in rates:
            raise CommandError(
                f"CurrencyLayer response did not include a {TARGET_CURRENCY} rate."
            )

        try:
            rate = Decimal(str(rates[TARGET_CURRENCY])).quantize(Decimal("0.0001"))
        except InvalidOperation as exc:
            raise CommandError(
                f"Received an unparseable {TARGET_CURRENCY} rate: "
                f"{rates[TARGET_CURRENCY]!r}."
            ) from exc

        if rate <= 0:
            raise CommandError(
                f"Received a non-positive {TARGET_CURRENCY} rate: {rate}."
            )

        if dry_run:
            self.stdout.write(
                f"[dry-run] would set ca_exchange_rate to {rate} "
                f"(1 {SOURCE_CURRENCY} = {rate} {TARGET_CURRENCY})."
            )
            return

        stats = SiteStats.load()
        previous = stats.ca_exchange_rate
        stats.ca_exchange_rate = rate
        stats.save(update_fields=["ca_exchange_rate"])

        self.stdout.write(
            self.style.SUCCESS(
                f"Updated ca_exchange_rate from {previous} to {rate} "
                f"(1 {SOURCE_CURRENCY} = {rate} {TARGET_CURRENCY})."
            )
        )
