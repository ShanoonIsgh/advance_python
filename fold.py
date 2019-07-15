from functools import reduce

total = reduce(lambda items, running_total: items + running_total, [1,2,3,4,5])
print(total)
