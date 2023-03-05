class Dequeue:
  def __init__(self):
    self.items = []

  def addRear(self, item):
    self.items.insert(0, item)
  
  def addFront(self, item):
    self.items.append(item)

  def removeRear(self):
    return self.items.pop(0)

  def removeFront(self):
    return self.items.pop()
  
  def isEmpty(self):
    return self.items == []
  
  def size(self):
    return len(self.items)


def palindromeChecker(word):
  iterableWord = "".join(word.split(' '))
  dequeue = Dequeue()

  for str in iterableWord:
    dequeue.addRear(str)
  
  stillEqual = True
  while dequeue.size() > 1 and stillEqual:
    first = dequeue.removeFront()
    last = dequeue.removeRear()

    if first != last:
      stillEqual = False
  
  return stillEqual


print(palindromeChecker('I PREFER PI'))
