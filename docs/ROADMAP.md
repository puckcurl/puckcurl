# Roadmap & Status

A light snapshot of what's built vs. planned.

### Still to build

- **Log a donation (API)** — `LogDonation` form exists in the UI but does **not** submit
  to the API yet, and there's no receipt-upload or donation-create endpoint yet (no DRF
  serializers/views over the models).
- **Charities / Plan views** — present but empty/stubbed.
- **`/donations` route** — declared in `constants.ROUTES` but has no view yet.

## Future ideas

- **Automatic goal/score import** — pull the player's scoring stats automatically
  from publicly available data instead of tracking them by hand.
- **Score alerts** — notify subscribed users when the player scores so they can consider
  donating again.
- **Email newsletter** - accept an optional email address when a user logs a donation. Send an email newsletter with updated total impact of the campaign.

## Out of scope (do not build)

- Accepting, processing, or facilitating donations / payments — this app only records
  donations made elsewhere.
