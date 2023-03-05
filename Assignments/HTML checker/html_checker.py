# Write a program that can check an HTML document for proper opening and closing tags.
# 1. Function receives block of html code
# 2. Iterate through string. if starts with <,letter append to queue...if </ deque till you get to <

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




def htmlChecker(html):
  htmlArr = html.split()
  htmlStack = Stack()
  print('**STARTING ARRAY**')
  print(htmlArr)

  for attribute in htmlArr:
    if attribute[0] in '<' and attribute[1].isidentifier():
     htmlStack.push(attribute)
    elif attribute.isidentifier():
      htmlStack.push(attribute)
    elif '</' in attribute:
      if htmlStack.isEmpty():
        return False
      else:
        topAttribute = htmlStack.pop() 
      while topAttribute.replace('<', '').replace('>', '') in attribute:
        if not htmlStack.isEmpty():
          topAttribute = htmlStack.pop()
        else:
          break
      
  if htmlStack.isEmpty():
    return True
  else:
    return False


txt = """<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>"""

print(htmlChecker(txt))
# print('<title>'.replace('<', '').replace('>', '') in '</title>')