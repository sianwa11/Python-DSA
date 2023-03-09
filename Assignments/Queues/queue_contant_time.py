class Node:
  def __init__(self, initData) -> None:
    self.data = initData
    self.next = None
    self.prev = None
  
  def getData(self):
    return self.data

  def setData(self, newData):
    self.data = newData

  def getNext(self):
    return self.next
  
  def setNext(self, nextData):
    self.next = nextData

  def getPrevious(self):
    return self.prev

  def setPrevious(self, prevData):
    self.prev = prevData


class Queue:
  def __init__(self) -> None:
    self.head = None
    self.tail = None

  def __str__(self) -> str:
    result = "["
    node = self.head
    if node:
      result += str(node.getData())
      node = node.getNext()
      while node:
        result += ", " + str(node.getData())
        node = node.getNext()
    result += "]"
    return result

  def enqueue(self, item):
    temp = Node(item)
    if self.head == None:
      self.head = temp
      self.tail = temp
    else:
      temp.setPrevious(self.tail)
      self.tail.setNext(temp)
      self.tail = temp

  def dequeue(self):
    if self.head == None:
      return
    else:
      self.head = self.head.getNext()




q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)

q.dequeue()
print(q)

q.dequeue()
print(q)
q.enqueue(30)
q.enqueue(41)
q.dequeue()
print(q)
q.dequeue()
print(q)

