# MLS Compliance Rules

The compliance engine strips flagged language before it reaches MLS remarks or NWMLS fields. See `Backend/models/compliance_filters.py`.

## Prohibited terms (current placeholder list)

- Subjective adjectives: "beautiful", "stunning", "luxurious", "perfect"
- Puffery: "won't last long", "act fast"
- Fair-housing violations: "safe neighborhood", "family-friendly", "great schools"

## Known gaps

- `sanitize()` currently does a plain, case-sensitive string replace — it will miss
  "Beautiful" (capitalized), partial-word matches, or paraphrased puffery.
- No fair-housing term list beyond the three examples above; NWMLS and HUD guidance
  should be reviewed to expand this before production use.
