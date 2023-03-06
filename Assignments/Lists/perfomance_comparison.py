import timeit
import random
from unordered_list import UnorderedList

unorderedList = UnorderedList()
pythonList = list()

print('-------------------------------------------------------------')
print("index, append(pythonList), append(unorderedList)")
for i in range(10000, 1000001,10000):
  t = timeit.Timer("pythonList.append(random.randrange(%d))"%i, "from __main__ import random, pythonList")
  t2 = timeit.Timer("unorderedList.append(random.randrange(%d))"%i, "from __main__ import random, unorderedList")

  pythonList_time = t.timeit(number=1000)
  unorderedList_time = t2.timeit(number=1000)

  print("%d,%10.3f,%10.3f" % (i,pythonList_time, unorderedList_time))
