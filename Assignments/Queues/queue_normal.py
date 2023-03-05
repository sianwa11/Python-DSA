class Queue:

  def __init__(self):
    self.items = []

  def enqueue(self, item):
    return self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()
  
  def isEmpty(self):
    return self.items == []
  
  def size(self):
    return len(self.items)


# q = Queue()
# q.enqueue('Morning routine')
# q.enqueue('Wake up')
# q.enqueue('Stretch')
# q.enqueue('Take a shit')
# q.enqueue('Get out of bed')
# q.dequeue()

# print(q.size())