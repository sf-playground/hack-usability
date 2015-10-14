# Usability and the Hack Typeface

The design of any typeface is a balance between two strong forces; the subjective _identity_ in the left corner vs. the objective _usability_ in the right. Because a programmar's typeface is such an important part of his toolset, the primary focus of the design tends to favor usability over identity; or in differents words _form follows function_.

- Read our [usability rationale](USABILITY.md) in more detail

## Primary objectives

To guide our efforts, we use the following assumptions to narrow down infinity to something graspable:

1. Hack is a typeface for _source code_, and is primarily used to display `ASCII`-characters.
2. Hack is not limited to a specific platform or environment.
3. Hack is used with type-size between _8px_ and _14px_.
4. Hack is used with a line-height between _100%_ and _150%_.
5. Hack aims to be an acceptible typeface for source code _without_ syntax highlighting.
6. Hack is tested with the most common programming languages; Javascript, Python, Ruby, Java, PHP, Markdown, CSS, HTML and C/C++.

This does not mean that issues that fall outside of these parameters are ignored. Any valid use-case that helps us improve the overall usability of Hack will be embraced.

- [Create](https://github.com/chrissimpkins/Hack/issues/new) or [View](https://github.com/chrissimpkins/Hack/issues) issues over at the main [Hack repository](https://github.com/chrissimpkins/Hack)

---

## Design guidelines

Our unscientific approach has led to the discovery that the stroke-width of Hack closests approximates `1px` when the type-size is set to `12px`. From that, we extrapolated a framework to objectively assess our glyph design, and established a few guidelines to follow when (re)designing glyphs.

- [Design guidelines](guidelines/GUIDELINES.md)

---

## Usability research

The assessment of usability issues is rather complex, and our methods are far from perfect. A change to a single glyph has to be considered across a range of different sizes, weights, styles, programming pattern contexts, different rendering types/platforms, and in combination with technically all other glyphs.

- [How to assess an usability issue](research/HOW_TO.md)
- Our reference of [language-specimens](https://github.com/sf-playground/language-specimens) used in testing

### Cases

The list of cases below displays some of the design considerations made to meet our criteria for acceptable usability. We use these to explain _why_ our `1` looks the way it does.

- [Angle brackets](research/cases/angle-brackets.md): `<` and `>`
- [Vertical characters](research/cases/verticals.md): `1`, `l`, `|`, `i` and `I`
- TODO [Horizontal characters](research/cases/horizontals.md): `-`, `_`, `=`
- TODO [Mathematical characters](research/cases/mathematical.md): `0-9`, `+`, `-`, `*`, `=`, `/`, `%`, `(`, `)`
- TODO [Round brackets](research/cases/round-brackets.md): `(` and `)`
- TODO [Curly brackets](research/cases/curly-brackets.md): `{` and `}`
- TODO [Square brackets](research/cases/square-brackets.md): `[` and `]`

---

## Contributions

If you would like to contribute to Hack or specifically the usability part, feel free to start discussions by [creating an issue]() or sending in your PR's. You can also contact @burodepeper (usability) or @chrissimpkins (identity) directly.

Contributions to our [language-specimens](https://github.com/sf-playground/language-specimens) are also very welcome. Our own practical knowledge is of course limited to certain areas.

References to interesting articles or useful tools are also welcome. We are open to improvement on every front.
