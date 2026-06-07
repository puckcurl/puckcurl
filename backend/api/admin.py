from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    actions = ("approve", "reject")

    def response_change(self, request, obj):
        if "_verify" in request.POST:
            if obj.is_verified:
                self.message_user(
                    request, "Donation is already verified.", level=messages.WARNING
                )
            else:
                obj.verified = timezone.now()
                obj.verified_by = request.user
                obj.save(update_fields=["verified", "verified_by"])
                self.message_user(request, "Donation verified.", level=messages.SUCCESS)
            return HttpResponseRedirect(request.get_full_path())
        if "_reject" in request.POST:
            if obj.is_verified:
                self.message_user(
                    request,
                    "Cannot reject a verified donation.",
                    level=messages.ERROR,
                )
                return HttpResponseRedirect(request.get_full_path())
            obj.delete()
            self.message_user(request, "Donation rejected.", level=messages.SUCCESS)
            return HttpResponseRedirect(reverse("admin:api_donation_changelist"))
        return super().response_change(request, obj)

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

    @admin.action(description="Reject selected donations")
    def reject(self, request, queryset):
        drafts = queryset.filter(verified__isnull=True)
        skipped = queryset.filter(verified__isnull=False).count()
        deleted = drafts.count()
        drafts.delete()
        if skipped:
            self.message_user(
                request,
                f"Skipped {skipped} verified donation(s); verified donations "
                "cannot be rejected.",
                level=messages.WARNING,
            )
        self.message_user(request, f"Rejected {deleted} donation(s).")


@admin.register(SiteStats)
class SiteStatsAdmin(admin.ModelAdmin):
    """Singleton: edit-only. No adding a second row, no deleting the one row."""

    def has_add_permission(self, request):
        return not SiteStats.objects.exists()  # ty: ignore[unresolved-attribute]

    def has_delete_permission(self, request, obj=None):
        return False
