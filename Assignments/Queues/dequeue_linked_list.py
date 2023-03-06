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


class DequeueLinkedList():
  def __init__(self):
    self.rear = None
    self.front = None

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

  def addFront(self, item):
    temp = Node(item)
    current = self.rear
    stop = False

    while current != None and not stop:
      if current.getNext() == None:
        stop = True
      else:
        current = current.getNext()
    
    if self.rear == None:
      self.rear = temp
      self.front = temp
    else:
      current.setNext(temp)

  def addRear(self, item):
    temp = Node(item)

    if self.rear == None:
      self.rear = temp
      self.front = temp
    else:
      temp.setNext(self.rear)
      self.rear = temp
    pass

  def removeFront(self):
    previous = None
    current = self.rear
    stop = False
    
    while current != None and not stop:
      if current.getNext() == None:
        stop = True
      else:
        previous = current
        current = current.getNext()
    
    if previous == None:
      self.rear = None
      self.front = None
    else:
      previous.setNext(None)
    
    return current.getData()

  def removeRear(self):
    current = self.rear
    nextNode = self.rear.getNext()
    if self.rear != None:
      self.rear = nextNode
    
    return current.getData()
    
  def size(self):
    count = 0
    current = self.rear

    while current != None:
      count = count + 1
      current = current.getNext()
  
    return count


dq = DequeueLinkedList()
print(dq.isEmpty())
dq.addFront(1)
dq.addFront(2)
dq.addFront(3)
dq.addRear(0)
dq.addRear(-1)
print(dq)

print(dq.removeFront())
print(dq)

print(dq.removeRear())
print(dq)



def palindromeChecker(string):
  dq = DequeueLinkedList()

  for letter in string:
    dq.addRear(letter)

  stillEqual = True
  while dq.size() > 1 and stillEqual:
    front = dq.removeFront()
    rear = dq.removeRear()

    if front != rear:
      stillEqual = False
  
  return stillEqual



print(palindromeChecker('bob'))
      