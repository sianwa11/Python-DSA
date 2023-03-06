from copy import copy

class Node:
  def __init__(self,initdata):
      self.data = initdata
      self.next = None

  def getData(self):
      return self.data

  def getNext(self):
      return self.next

  def setData(self,newdata):
      self.data = newdata

  def setNext(self,newnext):
      self.next = newnext


class UnorderedList:
  def __init__(self):
      self.head = None
      self.nodes = []

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

  def iterate_item(self):
    # Iterate the list.
    current_item = self.head
    while current_item:
        val = current_item.getData()
        current_item = current_item.getNext()
        yield val

  def isEmpty(self):
    return self.head == None

  def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
    self.nodes.append(self.head)

  def length(self):
    return len(self.nodes)

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
      self.nodes.pop()
    else:
      previous.setNext(current.getNext())
      self.nodes.pop()

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
        self.nodes.pop()
  
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

  # O(1) append
  def append_O1(self, item):
    pass


# linked = UnorderedList()

# linked.add('PHP')
# linked.add('HTML')
# linked.add('JS')
# linked.add('HTML')
# linked.add('Node')

# print(linked.size())
# print(linked.length())
# print(linked)
# linked.insert(2, 'Python')
# print(linked)
# linked_copy = linked.slice_(0,3)
# print(linked_copy)
# linked_copy.insert(2, 'Python')
# print(linked_copy)
