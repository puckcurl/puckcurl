import uuid
from decimal import Decimal

import django.core.validators
from django.db import migrations, models


def populate_tokens(apps, schema_editor):
    DonationReceipt = apps.get_model("api", "DonationReceipt")
    for receipt in DonationReceipt.objects.filter(token__isnull=True):
        receipt.token = uuid.uuid4()
        receipt.save(update_fields=["token"])


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_donation_effective_exchange_rate_and_more"),
    ]

    operations = [
        # Add nullable first so existing rows don't collide on the unique index.
        migrations.AddField(
            model_name="donationreceipt",
            name="token",
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.RunPython(populate_tokens, migrations.RunPython.noop),
        # Now enforce uniqueness and non-null.
        migrations.AlterField(
            model_name="donationreceipt",
            name="token",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        # Reject a zero/negative exchange rate at the source.
        migrations.AlterField(
            model_name="sitestats",
            name="ca_exchange_rate",
            field=models.DecimalField(
                decimal_places=4,
                default=Decimal("1.0000"),
                help_text="Canadian dollars per 1 USD.",
                max_digits=10,
                validators=[
                    django.core.validators.MinValueValidator(Decimal("0.0001"))
                ],
            ),
        ),
    ]
