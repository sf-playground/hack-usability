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

|                              | glyph box dimensions      | bearing      | character                   | relative sizes                     |
| typeface        | metrics    | height | width | x-height | left | right | width | height | center x,y | offset | outside | inside | stroke |
| --------------- | ---------- | ------ | ----- | -------- | ---- | ----- | ----- | ------ | ---------- | ------ | ------- | ------ | ------ |
| Hack            | 2048 - 492 | 1556   | 1233  | 1120     | 296  | 478   | 37.2% |  89.1% | 525.5, 642 |  -7.3% | 24.0%   | 60.2%  | 15.8%  |
| Input Mono      | 1100 - 250 | 850    | 662   | 600      | 198  | 142   | 48.6% |  92.7% | 359, 300   |     0% | 29.9%   | 57.6%  | 12.5%  |
| Source Code Pro | 1000 - 250 | 750    | 600   | 480      | 208  | 122   | 45.0% |  90.8% | 343, 278   |  -7.9% | 34.7%   | 53.0%  | 12.3%  |
| M+1m            | 1000 - 140 | 860    | 500   | 500      | 125  | 105   | 54.0% |  91.0% | 260, 315   | -13.0% | 25.0%   | 60.2%  | 14.8%  |
| Monoid          | 1536 - 384 | 1152   | 1024  | 1024     | 360  | 134   | 51.8% | 109.7% | 625, 703   | -18.7% | 35.2%   | 52.3%  | 12.5%  |
| Ubuntu Mono     | 1000 - 165 | 835    | 500   | 520      | 113  | 114   | 54.6% | 104.0% | 249.5, 267 |  -1.3% | 22.6%   | 61.4%  | 16.0%  |

- `offset-y`: (((x-height / 2) - center.y) / x-height) * 100
- Hack is the only one where the stroke-width tapers.
- The `x` in Ubuntu Mono is only 89.2% of the x-height.
- TODO: inside space at bottom/top
- TODO: glyph ratio and x-height ratio

#### Conclusions

n(n)n k(k)k g(g)g 8(8)8 ()

- TODO

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


### Visual comparison (at 8px, 10px and 12px)

![](https://...)

- TODO insert screenshot
- TODO compare

## Comments and issues

- rounder...

## Examples

TODO
