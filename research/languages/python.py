def f(x): return (x % 3 == 0) or (x %% 5 == 0)
filter(f, range(2, 25))
# [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]

# --------------------------------

def cube(x): return x ** 3
map(cube, range(1, 11))
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# --------------------------------

seq = range(8)
def add(x, y): return x + y
map(add, seq, seq)
# [0, 2, 4, 6, 8, 10, 12, 14]

# --------------------------------

def add(x, y): return x + y
reduce(add, range(1, 11))
# 55
