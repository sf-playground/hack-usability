# Mathematical characters

- - [Discussion](https://github.com/sf-playground/hack-usability/issues/4)

The following characters are commonly used in source code to do or display math:
- numbers: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` and `9`
- operators: `+`, `-`, `*`, `/`, `%` and `^`
- comparison: `=`, `<`, `>` and `!`
- meta and support: `~`, `%`, `&`, `(`, `)`, `,` and `.`

The following keywords are often used:
- `Math`, `sin`, `log`, `tan`, `cos`, `ln`, `sqrt`, etc.

Common combinations:
- comparison: `<=`, `>=`, `==`, `!==`, `===`, `!==`
- operators: `+=`, `-=`, `*=`, `/=`, `~=`, `%=` (not sure if this one exists)
- decimals: `3.14`, `.25`
- negative numbers: `-273`
- exponent(ial?)s: `10^3`, `10.3e5`, `661.9e-2`

Common patterns:
- calculations: `1 + 2 = 3`, `3 - 4 = -1`, `5 * 6 = 30`, `7 / 8 = 0.875`, `9 % 4 = 1`
- tight calculations: `1+2=3`, `3-4=-1`, `5*6=30`, `7/8=.875`, `9%4=1`

## Usability considerations

- `+`, `-`, `*`, `=`, `~`, `<` and `>` are expected to be vertically centered, and aligned to each other.
- `/` is expected to align with numbers, and to literally slice through them.
- `%` is expected to be subjective to adjacent numbers.

- TODO nested parentheses
- TODO tight vs loose forms (analysis)
