# Round brackets: ( and )

- TODO link to [Discussion]()

## Common forms

- `function(variable, variable);` vs `function ( variable, variable );`
- `for ( var i = 0; i < 100; i++ ) {` vs `for(var i=0;i<100;i++){`
- `function(function(function(function())))`
- `var x = ((a * b) + (c * d) / e);` vs `x=((a*b)+(c*d)/e)`
- `$post->getComments()->sort("relevancy")[0]`

## Assumptions

- Most often used in combination with `<letters:lowercase>` and/or `<numbers>`.
- Vertical alignment is relative to `x-height`; size is relative to extenders and descenders.
- Language style-guides often dictate whether they have spacing around, or not.
- Horizontal positioning matters most without spacing. `n(n)`
- Chris intentionally changed the horizontal positioning to have the brackets appear more 'open'.
- The left bracket is mostly preceded and followed by letters, the right bracket by punctuation.
- A pair of round brackets is often empty.
- Must be easily distinguishable from other types of brackets.
- Left and right bracket are mirrored.

## Comparison to other typefaces

### Metric comparison

| typeface                     | glyph box dimensions      | bearing      | character                   | relative sizes                             | ratio
| name            | metrics    | height | width | x-height | left | right | width | height | center x,y | offset | outside | inside | edge  | stroke | box  | x-h  |
| --------------- | ---------- | ------ | ----- | -------- | ---- | ----- | ----- | ------ | ---------- | ------ | ------- | ------ | ----- | ------ | ---- | ---- |
| Hack            | 2048 - 492 | 1556   | 1233  | 1120     | 296  | 478   | 37.2% |  89.1% | 525.5, 642 |  -7.3% | 24.0%   | 60.2%  | 38.8% | 15.8%  | 0.79 | 0.91 |
| Input Mono      | 1100 - 250 | 850    | 662   | 600      | 198  | 142   | 48.6% |  92.7% | 359, 300   |     0% | 29.9%   | 57.6%  | 21.5% | 12.5%  | 0.78 | 0.91 |
| Source Code Pro | 1000 - 250 | 750    | 600   | 480      | 208  | 122   | 45.0% |  90.8% | 343, 278   |  -7.9% | 34.7%   | 53.0%  | 20.3% | 12.3%  | 0.80 | 0.80 |
| M+1m            | 1000 - 140 | 860    | 500   | 500      | 125  | 105   | 54.0% |  91.0% | 260, 315   | -13.0% | 25.0%   | 60.2%  | 21.0% | 14.8%  | 0.58 | 1.00 |
| Monoid          | 1536 - 384 | 1152   | 1024  | 1024     | 360  | 134   | 51.8% | 109.7% | 625, 703   | -18.7% | 35.2%   | 52.3%  | 13.1% | 12.5%  | 0.89 | 1.00 |
| Ubuntu Mono     | 1000 - 165 | 835    | 500   | 520      | 113  | 114   | 54.6% | 104.0% | 249.5, 267 |  -1.3% | 22.6%   | 61.4%  | 22.8% | 16.0%  | 0.60 | 1.04 |

- `offset-y`: (((x-height / 2) - center.y) / x-height) * 100
- Hack is the only one where the stroke-width tapers.
- The `x` in Ubuntu Mono is only 89.2% of the x-height.

### Visual comparison (up-close)

- **Hack**
  - Most stylish
  - Significant breathing room on the inside
  - Alignment to `n` is just off-balance
  - Alignment to `k` feels natural
  - Alignment to `g` is okay
  - Alignment to `8` is clearly off-balance
  - The empty pair looks almost 3D

- **Input Mono**
  - Looks almost deconstructed to fit into pixels
  - Well balanced between inside and outside
  - Brackets are really round
  - Alignment to `n` is good
  - Alignment to `k` is good
  - Alignment to `g` feels cluttered at the bottom (brackets are too round perhaps)
  - Alignment to `8` is clearly off-balance
  - The empty pair forms a nice shape

- **Source Code Pro**
  - Nice balance between x-height and glyph width
  - Well balanced between inside and outside
  - Brackets are round, but open (compared to Input Mono); the exiting angle is pleasant
  - Alignment to `n` is good, perhaps a little to high
  - Alignment to `k` is good, surprisingly
  - Alignment to `g` is acceptable; the `g` is relatively complex
  - Alignment to `8` is not optimal, but acceptable, because the brackets are taller than the `8`
  - Empty pair feels natural

- **M+1m**
  - Narrow glyphs, not my personal preference
  - More space inside than out
  - Brackets themselves feel somewhat skewed
  - Alignment to `n` is clearly off-balance, _don't go low enough_
  - Alignment to `k` is good
  - Alignment to `g` is acceptable, but again, the brackets feel too high up
  - Alignment to `8` is feels off, brackets are not tall enough, or `8` is too tall
  - Empty pair feel generic, doesn't feel fixed-width

- **Monoid**
  - Curves are flattened, and feel big
  - Balance in and out is good, but brackets are too high up
  - Alignment to `n` is acceptable, but brackets end unexpectedly soon
  - Alignment to `k` is good
  - Alignment to `g` feels unnatural
  - Alignment to `8` is almost perfect
  - Empty pair is okay, but you feel that the curve is off

- **Ubuntu Mono**
  - Nice contrast between stroke-width and negative-space
  - More space inside than outside
  - Alignment to `n` is good
  - Alignment to `k` is good
  - Alignment to `g` is unexpectedly good
  - Alignment to `8` is more than acceptable
  - These brackets exactly surround all the other glyphs
  - Empty pair feels natural

### Visual comparison (at 10px, 12px and 14px)

![](https://raw.githubusercontent.com/sf-playground/hack-usability/master/images/parentheses.png)

Rendered in Atom (so Chrome), with subpixel rendering.

1. Hack
2. Input Mono
3. Source Code Pro
4. M+1m
5. Monoid
6. Ubuntu Sans

- **Hack**
  - Wider internal space gives priority of content over context
  - Letter clarity tied for first place with M+1m
  - `g` and `8` can be better 'contained'

- **Input Mono**
  - Good horizontal balance
  - Vertical position of brackets is a little low

- **Source Code Pro**
  - Significant lower x-height (nice `k`)
  - Good horizontal balance
  - Contains glyphs best, even at lower sizes

- **M+1m**
  - Vertical balance clearly off; too high
  - Horizontal balance good
  - Containment of `8` and empty pair outstanding

- **Monoid**
  - Vertical balance clearly off; far too high
  - Horizontal balance a bit wonky, but okay
  - Very clear letters at lower sizes
  - Brackets are clearly not round

- **Ubuntu Sans**
  - Looks better large than small
  - Horizontal balance not optimal, similar to Hack
  - Containment alsof off balance, too cramped
  - Most acceptable at 10px

#### Conclusions for Hack

- The `character-width` is considerably smaller than the average. This is mainly because of 'less roundness'. The roundness seems more than enough to be distinguisable though. The amount of space on the inside doesn't differ that much from average, so there's room for improvement there.
- In containing the four sample characters, Hack scores in the middle of the pack. Numbers and descenders can be better contained.
- When enlarged, the endings of the brackets would look better like Source Code Pro and Ubuntu Mono, as a line that is cut off.
- 'Source Code Pro' and 'M+1m' show a promise for improvement in Hack; the curve could be a bit rounder (towards a width of 45%) with a slight vertical offset to contain the `g` and numbers better; but those need analysis first.

## Comments and issues

- TODO 'could be rounder'
