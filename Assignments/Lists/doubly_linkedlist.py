class Node:
  def __init__(self, initData):
    self.data = initData
    self.next = None
    self.prev = None

  def getData(self):
    return self.data
  
  def setData(self, newData):
    self.data = newData

  def getNext(self):
    return self.next

  def setNext(self, nextItem):
    self.next = nextItem

  def getPrevious(self):
    return self.prev

  def setPrevious(self, prevItem):
    self.prev = prevItem


class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.node_dict = {}

  
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

  def isEmpty(self):
    return self.head == None

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.getNext()
    return count

  def add(self, item):
    temp = Node(item)
    if self.head == None:
      self.head = temp
      self.tail = temp
    else:
      temp.setPrevious(self.tail)
      self.tail.setNext(temp)
      self.tail = temp
    self.node_dict[item] = temp
  
  def remove(self, item):
    node_to_remove = self.node_dict.get(item)

    if node_to_remove is None:
      return

    if self.head.getData() == item:
      self.head = node_to_remove.getNext()

    if node_to_remove.getNext() != None:
      nextNode = node_to_remove.getNext()
      nextNode.setPrevious(node_to_remove.getPrevious())

    if node_to_remove.getPrevious() != None:
      prevNode = node_to_remove.getPrevious()
      prevNode.setNext(node_to_remove.getNext())
    
    del self.node_dict[item]


dbl = DoublyLinkedList()
dbl.add(1)
dbl.add(2)
dbl.add(3)
dbl.add(4)
dbl.add(5)
print(dbl)
    
dbl.remove(2)
print(dbl)