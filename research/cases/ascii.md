# ASCII characters

TODO an analysis of subgroups in ascii-characters and their relations

> ASCII includes definitions for 128 characters: 33 are non-printing control characters (many now obsolete) that affect how text and space are processed and _95 printable characters_, including the space (which is considered an invisible graphic.

The focus of this document is the analysis of the 95 printable characters in the ASCII definition. One could argue that:

1. these are the minimum required glyphs any typeface intended for source-code must include;
2. these make up the vast majority of characters found in source-code analysis;
3. a programmer's keyboard is capable of producing these glyphs without any 'special tricks'.

NOTE to @chrissimpkins: could you include details from your analysis about this?

## The characters (from hexadecimal 20 to 7E)

`space`, `!`, `"`, `#`, `$`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `-`, `.`, `/`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `:`, `;`, `<`, `=`, `>`, `?`, `@`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, `I`, `J`, `K`, `L`, `M`, `N`, `O`, `P`, `Q`, `R`, `S`, `T`, `U`, `V`, `W`, `X`, `Y`, `Z`, `[`, `\`, `]`, `^`, `_`, `backtick`, `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, `m`, `n`, `o`, `p`, `q`, `r`, `s`, `t`, `u`, `v`, `w`, `x`, `y`, `z`, `{`, `|`, `}`, `~`

Notes:

- German keyboards don't have standard keys for `\`, `[`, `]`, `{`, `|`, and `}`

### Subsets

#### `<punctuation>`

`!`, `"`, `#`, `$`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `-`, `.`, `/`, `:`, `;`, `<`, `=`, `>`, `?`, `@`, `[`, `\`, `]`, `^`, `_`, `backtick`, `{`, `|`, `}`, `~`

##### `<brackets>`

- `<brackets:round>` = `(` and `)`
- `<brackets:angle>` = `<` and `>`
- `<brackets:square>` = `[` and `]`
- `<brackets:curly>` = `{` and `}`

##### `<quotes>`

`"`, `'`, `backtick`

##### `<punctuation-in-text>`

`!`, `"`, `#`, `$`, `%`, `&`, `'`, `(`, `)`, `*`, `,`, `-`, `.`, `/`, `:`, `;`, `?`

#### `<numbers>`

`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`

#### `<letters>`

- `<letters:uppercase>'` = `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, `I`, `J`, `K`, `L`, `M`, `N`, `O`, `P`, `Q`, `R`, `S`, `T`, `U`, `V`, `W`, `X`, `Y` and `Z`
- `<letters:lowercase>` = `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, `m`, `n`, `o`, `p`, `q`, `r`, `s`, `t`, `u`, `v`, `w`, `x`, `y` and `z`

### Grouped by similarity or function

#### `<left>`

`(`, `<`, `[`, `{`, `/`

#### `<right>`

`)`, `>`, `]`, `}`, `\`

#### `<mathematical>`

`!`, `%`, `(`, `)`, `*`, `+`, `-`, `.`, `/`, `<`, `=`, `>`, `~`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`

#### `<horizontal>`

`+`, `-`, `<`, `=`, `>`, `_`, `~`

#### `<vertical>`

`!`, `(`, `)`, `+`, `/`, `:`, `;`, `[`, `\`, `]`, `{`, `|`, `}`, `1`, `7`, `I`, `J`, `L`, `T`, `i`, `j`, `l`

#### `<round>`

`@`, `0`, `8`, `C`, `D`, `G`, `O`, `Q`, `o`

#### `<tiny>`

`"`, `'`, `,`, `.`, `backtick`

#### `<separators>`

TODO

#### `<detailed>`

`#`, `$`, `%`, `&`, `*`, `0`, `@`, `a`, `e`, `m`, `s`, `w`, `~`

#### `<...>`

`g`, `9`, `q`

#### Stems

Assumptions:
- The stems of these characters (or at least of the subsets of these characters) vertically align. If any of these characters don't match up, it gives an off-balance feel.

##### `<center-stems>`

`!`, `$`, `+`, `1`, `:`, `;`, `I`, `J`, `T`, `Y`, `f`, `i`, `j`, `l`, `t`, `|`

##### `<left-stems>`

`5`, `B`, `D`, `E`, `F`, `H`, `K`, `L`, `M`, `N`, `P`, `R`, `U`, `[`, `b`, `h`, `k`, `m`, `n`, `p`, `r`, `u`

##### `<right-stems>`

`H`, `M`, `N`, `U`, `]`, `d`, `h`, `m`, `n`, `u`

#### `<curved-bottoms>`

TODO

### Relationships between glyphs

TODO
