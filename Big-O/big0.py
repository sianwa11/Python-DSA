numberList = [1,2,3,4,5,6,7,8,9,10]

def func1():
  minimum = 0
  for i in range(len(numberList)):
    isSmallest = True
    for j in range(len(numberList)):
      if(numberList[i] > numberList[j]):
        isSmallest = False
      if isSmallest:
        minimum = numberList[i]
  return minimum


def func2(list):
  smallest = list[0]
  for i in list:
    if(i < smallest):
      smallest = i
  return smallest


print(func1())
print(func2([5,20,16]))