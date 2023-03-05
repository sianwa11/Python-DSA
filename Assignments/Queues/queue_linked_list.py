# Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.
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

# Queue using linked list    
class QueueLinkedList:
  def __init__(self):
    self.rear = None
    self.front = None
  
  def enqueue(self, item):
    temp = Node(item)
    if self.rear == None:
      self.rear = temp
      self.front = temp
    else:
      self.rear.setNext(temp)
      self.rear = temp
  
  def dequeue(self):
    self.front = self.front.getNext()

    if self.front == None:
      self.rear = None


if __name__ == '__main__':
    q = QueueLinkedList()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    print("Queue Front : " + str(q.front.data if q.front != None else -1))
    print("Queue Rear : " + str(q.rear.data if q.rear != None else -1))