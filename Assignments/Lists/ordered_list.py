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

  def __str__(self) -> str:
    result = "["
    node = self.head
    if node != None:
      result += str(node.getData())
      node = node.getNext()
      while node:
          result += ", " + str(node.getData())
          node = node.getNext()
    result += "]"
    return result

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

       #allow duplicates
      elif current.getData() == item:
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

  def append(self, item):
    current = self.head
    stop = False
    previous = None

    while current != None and not stop:
      if current.getNext() != None:
        previous = current
        current = current.getNext()
      else:
        if previous.getData() < item:
          current.setNext(Node(item))
        stop = True

  def index(self, item):
    current = self.head
    count = 0
    stop = False

    while current != None and not stop:
      if current.getData() == item:
        stop = True
      else:
        count = count + 1
      current = current.getNext()
  
    return count

  def insert(self,pos,item):
    current = self.head
    previous = None
    stop = False
    count = 0
    temp = Node(item)

    while current != None and not stop:
      if pos == count:
        stop = True
      else:
        previous = current
        current = current.getNext()
        count = count + 1

    if previous == None:
      temp.setNext(current)
      current = temp
    else:
      if pos == count and item < current.getData():
        previous.setNext(temp)
        temp.setNext(current)

  def pop(self):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
      if current.getNext() == None:
        #remove current
        stop = True
      else:
        previous = current
        current = current.getNext()

    if previous != None:
      previous.setNext(None)

  def pop_(self, pos):
    current = self.head
    previous = None
    stop = False
    count = 0

    while current != None and not stop:
      if pos == count:
        stop = True
      else:
        previous = current
        current = current.getNext()
        count = count + 1
    
    if previous == None:
      self.head = current.getNext()
    else:
        previous.setNext(current.getNext())

# linked = OrderedList()
# linked.add(10)
# linked.add(20)
# linked.add(202)
# linked.add(30)
# linked.add(40)
# linked.append(2000)
# print(linked)
# print(linked.index(10))
# linked.insert(1,15)
# linked.insert(6,203)
# print(linked)
# linked.pop()
# print(linked)
# linked.pop()
# print(linked)
# linked.pop()
# print(linked)
# linked.pop()
# print(linked)
# linked.append(200)
# print(linked)
# linked.pop_(4)
# print(linked)

