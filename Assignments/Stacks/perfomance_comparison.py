import timeit
import random

# Import python List based Stack
from pythonds import Stack

# Import Linked List based Stack
from stack import StackList


linkedListStack = StackList()
pythonStack = Stack()

print('-------------------------------------------------------------')
print("index, push(pythonStack), push(linkedListStack)")
for i in range(10000, 100001, 10000):
  t = timeit.Timer("pythonStack.push(random.randrange(%d))"%i, "from __main__ import random, pythonStack")
  t2 = timeit.Timer("linkedListStack.push(random.randrange(%d))"%i, "from __main__ import random, linkedListStack")

  pythonStack_time = t.timeit(number=1000)
  linkedListStack_time = t2.timeit(number=1000)

  print("%d,%10.3f,%10.3f" % (i,pythonStack_time, linkedListStack_time))
