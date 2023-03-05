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
        self.tail = None
    

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


linked = UnorderedList()

# linked.add('PHP')
# linked.add('HTML')
# linked.add('JS')
linked.append('MySQL')
linked.append('CSS')

for val in linked.iterate_item():
  print(val)
