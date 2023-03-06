
class Node:
  def __init__(self, initData) -> None:
    self.data = initData
    self.next = None
  
  def getData(self):
    return self.data
  
  def setData(self, newData):
    self.data = newData

  def getNext(self):
    return self.next

  def setNext(self, next):
    self.next = next

class StackList:
  def __init__(self):
    self.head = None

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

  def push(self, item):
    temp = Node(item)
    current = self.head
    stop = False

    while current != None and not stop:
      if current.getNext() == None:
        stop = True
      else:
        current = current.getNext()

    if current == None:
      temp.setNext(self.head)
      self.head = temp
    else:
      current.setNext(temp)

  def pop(self):
    current = self.head
    previous = None
    stop = False

    while current != None and not stop:
      if current.getNext() == None:
        stop = True
      else:
        previous = current
        current = current.getNext()
    
    item = current.getData()
    if previous == None:
      self.head = None
    else:
      previous.setNext(None)
    
    return item

  def peek(self):
    current = self.head
    stop = False

    while current != None and not stop:
      if current.getNext() == None:
        stop = True
      else:
        current = current.getNext()
    
    return current.getData()

  def size(self):
    current = self.head
    count = 0

    while current != None:
      count = count + 1
      current = current.getNext()
    
    return count


# stack = StackList()
# stack.push('A')
# stack.push('B')
# stack.push('C')
# stack.push('D')
# stack.push('E')
# stack.push('F')
# stack.push('G')

# print(stack.size())
# print(stack)
# stack.pop()
# print(stack)