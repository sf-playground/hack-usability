# Python

## Operators

- `17 // 3.0`: explicit floor division discards the fractional part
- `17 % 3`: % returns the remainder of the division
- `5 ** 2`: 5^2, 5 squared
- `2 ** 7`: 2^7, 2 to the power 7th
- `3+5j`: 'j' indicates the imaginary part
- `in` and `not in`
- `is` and `is not`

## Strings

- `print r'C:\some\name'` prints a raw string, no escaped chars
- print multiline string, start with `"""\`, end with `"""`
- `3 * 'un' + 'ium'` gives 'unununium'
- `'Py' 'thon'` gives 'Python'
- get a character or slice with `word[3]` and `word[1:3]`; begin and end are optional, positions can be negative
- `u'Unicode'` and `ur'Unicode'` and `u'Hello\u0020World !'`
- > The default encoding is normally set to ASCII, which passes through characters in the range 0 to 127 and rejects any other characters with an error.
- `u"äöü".encode('utf-8')`
- `unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'utf-8')`

## Lists

- `squares = [1, 4, 9, 16, 25]`
- `squares[-3:]` returns `[9, 16, 25]`
- `[1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6]`
- `letters[2:5] = []` removes a slice
- `[['a', 'b', 'c'], [1, 2, 3]]` to nest lists

## Control flow tools

- `if <...>:`, `elif <...>:`, `else:`

## PEP 8

- Use 4-space indentation, and no tabs.
- Wrap lines so that they don't exceed 79 characters.
- Use blank lines to separate functions and classes, and larger block of code inside functions.
- When possible, put comments on a line of their own.
- Use docstrings.
- Use spaces around operators and after commas, but not directly inside bracketing constructs: `a = f(1, 2) + g(3, 4)`
- Name your classes functions consistently; `CamelCase` for classes and `lower_case_with_underscores` for functions and methods.
- Always use `self` as the name for the first method argument.
- Don't use fancy encodings if your code is meant to be used in international environments. Plain ASCII works best in any case.

## Data Structures
