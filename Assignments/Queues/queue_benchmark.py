# Design and implement an experiment to do benchmark comparisons of the two queue implementations. What can you learn from such an experiment?
# Answer: Enqueueing a Queue with a linked list implementation is faster than the list implementation of Queue
from queue_linked_list import QueueLinkedList
from queue_normal import Queue

import timeit
import random

queue_normal = Queue()
queue_linked_list = QueueLinkedList()

print('-------------------------------------------------------------')
print("index, enqueue (queue_normal), enqueue (queue_linked_list)")
for i in range(10000, 1000001,10000):
  t = timeit.Timer("queue_normal.enqueue(random.randrange(%d))"%i, "from __main__ import random,queue_normal")
  t2 = timeit.Timer("queue_linked_list.enqueue(random.randrange(%d))"%i, "from __main__ import random,queue_linked_list")

  queue_normal_time = t.timeit(number=1000)
  queue_linked_list_time = t2.timeit(number=1000)

  print("%d,%10.3f,%10.3f" % (i,queue_normal_time, queue_linked_list_time))

print('Queue normal size: ', queue_normal.size())

print('\n')
print('\n')
print('-------------------------------------------------------------')
print("index, dequeue (queue_normal), dequeue (queue_linked_list)")
for i in range(10000, 1000001,10000):
  t = timeit.Timer("queue_normal.dequeue()", "from __main__ import random,queue_normal")
  t2 = timeit.Timer("queue_linked_list.dequeue()", "from __main__ import random,queue_linked_list")

  queue_normal_time = t.timeit(number=1000)
  queue_linked_list_time = t2.timeit(number=1000)

  print("%d,%10.3f,%10.3f" % (i,queue_normal_time, queue_linked_list_time))

print('Queue normal size: ', queue_normal.size())


# It is possible to implement a queue such that both enqueue and dequeue have 
#  performance on average. In this case it means that most of the time enqueue and dequeue will be 
#  except in one particular circumstance where dequeue will be 

