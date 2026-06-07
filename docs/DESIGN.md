# Design System

A high level overview of color and font selections for the project and any supporting marketing materials.

The values below are the source of truth for marketing assets, in the app these are
implemented as theme tokens in `frontend/src/index.css` (`@theme`). **Always prefer the role
tokens over raw palette values** when styling.

## Color Palette

Each color is a full 50–950 scale; the hex shown is the root shade.

- `#36C4FC` - Sky Aqua (root `sky-aqua-400`)
- `#F6A2B3` - Cherry Blossom (root `cherry-blossom-200`)
- `#EFF2D9` - Cream (root `cream-100`)
- `#555577` - Space Indigo (root `space-indigo-600`)
- `#0C062D` - Dark Amethyst (root `dark-amethyst-900`)

## Surfaces & background

- `bg-page` - dark-amethyst-900 (the page surface)
- `bg-protest` - the signature background: the dark-amethyst page color overlaid with
  blue + pink radial gradients.

## Text

Body copy is cream; headings/accents are pink or blue. Muted/subtle/faint cover
secondary text.

- `text-body` - cream-50
- `text-heading-pink` - cherry-blossom-200 (Pink heading/accent)
- `text-heading-blue` - sky-aqua-400 (Blue heading/accent)
- `text-muted` - space-indigo-300
- `text-subtle` - space-indigo-700
- `text-faint` - space-indigo-800

## Borders

- `border-light` - slate-600
- `border-dark` - slate-800

## Fonts

- `font-heading` - Montserrat (headings; auto-applied to `h1`–`h6` via the base layer)
- `font-display` - Open Sans (body copy / default)
