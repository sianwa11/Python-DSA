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
    pass
      