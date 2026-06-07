from rest_framework import serializers

from api.models import Charity, Donation


class SiteStatsSerializer(serializers.Serializer):
    """Public, read-only campaign totals"""

    verified_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    verified_count = serializers.IntegerField()
    goals_scored = serializers.IntegerField()


class DonationSerializer(serializers.ModelSerializer):
    """Public, read-only view of a single verified donation"""

    name = serializers.CharField(source="get_name_display", read_only=True)
    charity = serializers.CharField(source="charity.name", read_only=True)

    class Meta:
        model = Donation
        fields = ["id", "created", "amount", "name", "charity"]


class CharitySerializer(serializers.ModelSerializer):
    """Public, read-only view of an approved charity"""

    class Meta:
        model = Charity
        fields = ["id", "name", "url"]
