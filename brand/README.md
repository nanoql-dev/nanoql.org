# nanoql brand files

The nanoql wordmark is "nanoql" with its "o" drawn as a solid dot. The mark is that dot ringed, with a thin white gap
and one pale ring around it, on a pale tile. The colours are ocean blues: deep navy letters, a sky-blue dot.

## Files

| File | Use |
|---|---|
| `nanoql-wordmark-light.svg` | The wordmark on light grounds |
| `nanoql-wordmark-dark.svg` | The wordmark on dark grounds |
| `nanoql-mark.svg` | The mark on its rounded tile, anywhere a square is needed |
| `favicon.svg`, `favicon.ico` | The browser's tab icon (the `.ico` holds 16, 32 and 48 px) |
| `apple-touch-icon.png` | 180 px, square: iOS rounds it itself |
| `nanoql-mark-{16,32,48,128,192,512}.png` | The mark as pictures: 128 px is NuGet's package icon |
| `nanoql-avatar.png` | 800 px, the tile run to the edges: profile pictures that round or crop themselves (LinkedIn, GitHub) |
| `nanoql-card.png` | 1200 × 630 px, the link-preview card every page names (`og:image`): the wordmark, the tagline in Space Grotesk 600 and the languages, on the home page's band |

On a 64-unit tile the ring's radius is 22, the gap's 14.25 and the dot's 13.25. At 16 and 32 px (`favicon.svg`, the
two smallest pictures and the `.ico`'s two smaller sizes) the ring is 23, the gap 15.5 and the dot 13, so that the gap
still shows.

## Colours

| | Ink | Dot |
|---|---|---|
| On light grounds | `#0C2D48` | `#0EA5E9` |
| On dark grounds | `#E0F2FE` | `#7DD3FC` |
| The mark | tile `#F0F9FF`, ring `#A5DDFB`, gap white | `#0EA5E9` |

The site's own colours go with them: page tint `#F0F9FF`, buttons and links `#0369A1`, and a dark mode on deep ocean
rather than black, the page and menu bar `#082F49` with the home page's band and the panels `#0C4A6E`
(`template/public/main.css`).

## Typeface

The letters are Space Grotesk at weight 600, by the Space Grotesk Project Authors, under the SIL Open Font License
1.1. Its kerning is kept and its tracking is −0.03 em. The letters are outlined in the files, so no font is needed to
show them. The dot is the size of the font's own "o", centred where the "o" sits. The site sets its headings in the
same typeface (`template/public/fonts/space-grotesk.woff2`, a Latin subset).

## Use

- Keep clear space around the wordmark of at least the dot's diameter.
- Show the wordmark at least 16 px tall on screen, and the mark at 16 px or more.
- Don't recolour, stretch, outline or add effects to either. Where only one colour is possible, draw both the
  letters and the dot in the ink colour.
- The one exception: in large artwork on a dark ground, such as a social preview card, the dot alone may carry a
  soft glow, brightest at its rim and fading outward. Never in the wordmark, the favicon or the menu bar.
