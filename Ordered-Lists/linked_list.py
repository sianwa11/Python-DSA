class Node:
  def __init__(self, initData):
    self.data = initData
    self.next = None

  def getData(self):
    return self.data
  
  def getNext(self):
    return self.next
  
  def setData(self, newData):
    self.data = newData
  
  def setNext(self, next):
    self.next = next


class OrderedList:
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def size(self):
    current = self.head
    count = 0

    while current != None:
      count = count + 1
      current = current.getNext()

    return count
  
  def remove(self, item):
    current = self.head
    previous = None
    found = False

    while not found:
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()
    
    if previous == None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())

  def search(self, item):
    current = self.head
    found = False
    stop = False

    while current != None and not found and not stop:
      if current.getData() == item:
        found = True
      else:
        if current.getNext() > item:
          stop = True
        else:
          current = current.getNext()
    
    return found
  
  def add(self, item):
    current = self.head
    previous = None
    stop = False
    temp = Node(item)

    while current != None and not stop:
      if current.getData() > item:
       stop = True
      else:
        previous = current
        current = current.getNext()

    if previous == None:
      temp.setNext(self.head)
      self.head = temp
    else:
      temp.setNext(current)
      previous.setNext(temp)

