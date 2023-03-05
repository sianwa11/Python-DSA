class Stack:

  def __init__(self):
    self.items = []
  
  def __str__(self) -> str:
    return " ".join(self.items)

  def isEmpty(self):
    return self.items == []
  
  def push(self, item):
    return self.items.append(item)
  
  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) - 1]

  def size(self):
    return len(self.items)


# Reverse a string using stack
# def revString(str):
#   s = Stack()
#   for i in str:
#     s.push(i)
#   revString = ''

#   while not s.isEmpty():
#     revString = revString + s.pop()
#   return revString

# def covert2Binary(num):
#   s = Stack()

#   while num > 0:
#       rem = num % 2
#       s.push(rem)
#       num = num // 2

#   binary = ""
#   while not s.isEmpty():
#       binary = binary + str(s.pop())

#   return binary



# print(revString('banana'))
# print(covert2Binary(233))