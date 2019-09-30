#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ["abv", "Abv", "dfs", "dfs", "DFs", "sdf", "dfw"]

# Реализация задания 2
print(*list(data2), sep=', ')
distinct = Unique(data3, ignore_case=False)
for item in distinct:
    print(item, end=' ')
