# Modify the Hot Potato simulation to allow for a randomly chosen counting value so that each pass is not predictable from the previous one

from pythonds.basic.queue import Queue
import random


def hotPotatoe(nameList,num):

  simqueue = Queue()

  for name in nameList:
    simqueue.enqueue(name)

  while simqueue.size() > 1:

    for i in range(num):
      simqueue.enqueue(simqueue.dequeue())

    simqueue.dequeue()


  return simqueue.dequeue()


print(hotPotatoe(['Neema','Sianwa', 'Manka', 'Baraka'], random.randrange(1,11)))