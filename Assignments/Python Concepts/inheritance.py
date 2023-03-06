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

class LinkedList:
  def __init__(self):
    self.head = None
  
  def isEmpty(self):
    return self.head == None

  def __str__(self):
    result = '['
    node = self.head
    if node:
      result += str(node.getData())
      node = node.getNext()
      while node:
        result += ', ' + str(node.getData())
        node = node.getNext()
      result += ']'
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

    while not found and current != None:
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()
    
    if previous == None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())


class UnorderedList(LinkedList):
  def __init__(self):
    super(UnorderedList, self).__init__()

  def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp

  def size(self):
    current = self.head
    count = 0

    while current != None:
      count = count + 1
      current = current.getNext()
    
    return count

  def search(self, item):
    current = self.head
    found = False

    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()
    
    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False

    while not found and current != None:
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()
    
    if not found:
      print('not found')
      return
    
    if previous == None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())

  def index(self, item):
    current = self.head
    found = False
    count = 0

    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()
        count = count + 1

    return count

  def pop(self):
    current = self.head
    previous = None
    found =  False

    while current != None and not found:
      if current.getNext() != None:
        previous = current
        current = current.getNext()
      else:
        item = current.getData()
        current = None
        previous.setNext(current)
  
    return item

  def insert(self, pos, item):
    current = self.head
    found = False
    previous = None
    count = 0
    temp = Node(item)

    while current != None and not found:
      if pos == count:
        found = True
      else:
        previous = current
        current = current.getNext()
        count = count + 1
    
    if previous == None:
      temp.setNext(current)
      current = temp
    else:
      if count == pos:
        previous.setNext(temp)
        temp.setNext(current)
  
  # Implement a slice method for the UnorderedList class. It should take two parameters, start and stop, and return a copy of the list starting at the start position and going up to but not including the stop position.
  def slice_(self, start, stop):
    current = self.head
    lListArr = []
    count = 0
    stopCount = False
    while current != None and not stopCount:
      if count == stop:
        stopCount = True
      elif count >= start:
        lListArr.append(current.getData())

      count = count + 1
      current = current.getNext()
    
    link = UnorderedList()
    for node in lListArr[::-1]:
      link.add(node)

    return link

  # O(n) append
  def append(self, item):
    current = self.head

    if current:
      while current.getNext() != None:
        current = current.getNext()
      current.setNext(Node(item))
    else:
      self.head = Node(item)



class OrderedList(LinkedList):
  def __init__(self):
    super().__init__()

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




unorderedList = UnorderedList()
unorderedList.add('HTML')
unorderedList.add('CSS')
unorderedList.add('JS')
unorderedList.add('PHP')
print(unorderedList)
unorderedList.append('jaja')
print(unorderedList)


orderedList = OrderedList()
orderedList.add(10)
orderedList.add(23)
orderedList.add(1)
orderedList.add(11)
print(orderedList)
orderedList.append(25)
print(orderedList)