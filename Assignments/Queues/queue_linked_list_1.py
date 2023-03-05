class Node:
  def __init__(self,initData) -> None:
    self.data = initData
    self.next = None

  def getData(self):
    return self.data
  
  def setData(self, newData):
    self.data = newData
  
  def getNext(self):
    return self.next

  def setNext(self, newNext):
    self.next = newNext


class QueueLinkedList:
  def __init__(self):
    self.front = None
    self.rear = None

  def isEmpty(self):
    return self.rear == None

  def __str__(self) -> str:
    result = "["
    node = self.rear
    if node != None:
      result += str(node.getData())
      node = node.getNext()
      while node:
          result += ", " + str(node.getData())
          node = node.getNext()
    result += "]"
    return result
  
  def size(self):
    current = self.rear
    count = 0
    while current != None:
      count = count + 1
      current = current.getNext()
    return count

  def enqueue(self, item):
    temp = Node(item)
    if self.rear == None:
      self.rear = temp
      self.front = temp
    else:
      temp.setNext(self.rear)
      self.rear = temp

  def dequeue(self):
    current = self.rear
    previous = None
    found =  False

    while current != None and not found:
      if current.getNext() != None:
        previous = current
        current = current.getNext()
      else:
        current = None
        previous.setNext(current)
  

queueLinked = QueueLinkedList()
print(queueLinked.isEmpty())
print(queueLinked.size())

queueLinked.enqueue(10)
queueLinked.enqueue(20)
queueLinked.enqueue(30)
queueLinked.enqueue(40)

print(queueLinked.isEmpty())
print(queueLinked.size())
print(queueLinked)

queueLinked.dequeue()
print(queueLinked)
print(queueLinked.size())

queueLinked.dequeue()
print(queueLinked)
print(queueLinked.size())