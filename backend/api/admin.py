from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

from api.models import Charity, Donation, DonationReceipt, SiteStats


@admin.register(Charity)
class CharityAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "approved", "created")
    list_filter = ("approved",)
    search_fields = ("name", "url")
    actions = ("approve",)

    @admin.action(description="Approve selected charities")
    def approve(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f"Approved {updated} charit(ies).")


@admin.register(DonationReceipt)
class DonationReceiptAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created", "file_link")
    readonly_fields = ("created", "file_link")

    @admin.display(description="File")
    def file_link(self, obj):
        if not obj.file:
            return "—"
        return format_html(
            '<a href="{}" target="_blank">View receipt</a>', obj.file.url
        )


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("amount", "name", "charity", "is_verified", "created")
    list_filter = ("verified", "charity")
    search_fields = ("name",)
    readonly_fields = ("created", "verified", "verified_by", "receipt_link")
    autocomplete_fields = ("charity",)
    actions = ("approve",)

    @admin.display(boolean=True, description="Verified")
    def is_verified(self, obj):
        return obj.is_verified

    @admin.display(description="Receipt")
    def receipt_link(self, obj):
        if not obj.receipt_id or not obj.receipt.file:
            return "—"
        return format_html(
            '<a href="{}" target="_blank">View receipt</a>', obj.receipt.file.url
        )

    @admin.action(description="Approve selected donations")
    def approve(self, request, queryset):
        updated = queryset.filter(verified__isnull=True).update(
            verified=timezone.now(), verified_by=request.user
        )
        self.message_user(request, f"Approved {updated} donation(s).")


@admin.register(SiteStats)
class SiteStatsAdmin(admin.ModelAdmin):
    """Singleton: edit-only. No adding a second row, no deleting the one row."""

    def has_add_permission(self, request):
        return not SiteStats.objects.exists()  # ty: ignore[unresolved-attribute]

    def has_delete_permission(self, request, obj=None):
        return False
