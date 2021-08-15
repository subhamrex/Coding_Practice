# [print(x) for x in range(1, 100) if not list(filter(lambda y: (x % y) == 0, range(2, x - 1)))] 
[print(p) for p in range(2,101) if not [q for q in range(2, p-1) if not p%q]]