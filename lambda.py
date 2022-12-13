key = lambda x: (-x[0], x[1])
lst = [(2, 10),(2, 20), (2, 30), (2, 40)]
print(sorted(lst, key=key))