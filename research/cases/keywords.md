# Keywords

## Python

### Patterns

- `"string".function()`
- `list = [1, 2, 3]`
- `len("string")` not `"string".len()`
- assignment: `a, b = 0, 1` and `a, b = b, a+b`
- `while b < 10:`
- `print b,` avoids new-line
- `for w in words:`, indent lines after that
- `if <...>:`, `elif <...>:`, `else:`
- `[].insert()`
- `class MyClass:`
- `def fib(n):`
- `def initlog(*args):`
- `def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):`
- `parrot(1000, action='VOOOM!')`; position vs keyword arguments
- `def function(type, *tuple, **dictionary):`; * = all position arguments, ** = all keyword arguments
- tuple = ()
- list = array = []
- set = {} = object without keys, and unique values
- dictionary = {} = object with key:value, and thus unique keys
- `print "-" * 40` prints a line of 40 dashes
- `separator.join(arguments)` (NOTE: seems inverted)
- `pairs.sort(key=lambda pair: pair[1])`
- `def f(x): return x % 3 == 0 or x % 5 == 0`
- `squares = [x**2 for x in range(10)]`
- `[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]`
- `if not ...:`
- `for ... in ...:`

### Functions

- encode()
- insert()
- int()
- [].keys()
- len()
- print()
- range()
- raw_input()
- round()
- sorted(), `sorted(keywords.keys())`
- str()
- "".strip()
- sum([])
- unicode()
- zip()

#### Lists

- append(), extend(), insert(), remove(), pop(), index(), count(), sort(), reverse()
  - [].append(x)
  - [].extend(L)
  - [].insert(i, x)
  - [].remove(x)
  - [].pop(i)
  - [].index(x)
  - [].count(x)
  - [].sort(cmp=None, key=None, reverse=False)
  - [].reverse()
  - len([])
- collections.deque, deque(), popleft()
- filter(), map(), reduce()
- `for key, value in items.iteritems():`

### Keywords

- if, elif, else
- while, for
- break, continue, pass
- True, False, None
- class
- def, return
- raise, IOError()
- lambda
- del
- not, and, or
