import timeit
import random


# def test1():
#     l = []
#     for i in range(1000):
#         l = l + [i]

# def test2():
#     l = []
#     for i in range(1000):
#         l.append(i)

# def test3():
#     l = [i for i in range(1000)]

# def test4():
#     l = list(range(1000))

# t1 = Timer("test1()", "from __main__ import test1")
# print("concat ",t1.timeit(number=1000), "milliseconds")
# t2 = Timer("test2()", "from __main__ import test2")
# print("append ",t2.timeit(number=1000), "milliseconds")
# t3 = Timer("test3()", "from __main__ import test3")
# print("comprehension ",t3.timeit(number=1000), "milliseconds")
# t4 = Timer("test4()", "from __main__ import test4")
# print("list range ",t4.timeit(number=1000), "milliseconds")

# popzero = Timer("x.pop(0)",
#                 "from __main__ import x")
# popend = Timer("x.pop()",
#                "from __main__ import x")
# print("pop(0)   pop()")
# for i in range(1000000,100000001,1000000):
#     x = list(range(i))
#     pt = popend.timeit(number=1000)
#     x = list(range(i))
#     pz = popzero.timeit(number=1000)
#     print("%15.5f, %15.5f" %(pz,pt))

# for i in range(10000, 1000000, 20000):
#     t = timeit.Timer("x[random.randrange(%d)]"%i,
#                      "from __main__ import random, x")


#     x = list(range(i))
#     indextime = t.timeit(number=100)
#     print("%d, %10.4f" %(i, indextime))

# print("index,  get item,  set item")
# for i in range(10000,1000001,20000):
#     t = timeit.Timer("x[random.randrange(%d)]"%i,
#                      "from __main__ import random,x")
#     t2 = timeit.Timer("x[random.randrange(%d)] = %s" %(i,random.randrange(i)),
#                      "from __main__ import random,x")
  
#     x = {j:None for j in range(i)}
#     d_time = t.timeit(number=1000)
#     s_time = t2.timeit(number=1000)
#     print("%d,%10.3f,%10.3f" % (i,d_time,s_time))

# print("index,  delete list,  delete dictionary")
# for i in range(10000, 1000001,20000):
#   # t = timeit.Timer("del x[random.randrange(%d)]"%i, "from __main__ import random,x")
#   x =  list(range(i))
#   xl = {j:None for j in range(i)}
  
#   t = timeit.Timer("del x[random.randrange(len(x))]",
#                      "from __main__ import random, x")
#   t2 = timeit.Timer("del xl[random.choice(list(xl.keys()))] ",
#                      "from __main__ import random, xl")

#   list_time = t.timeit(number=1000)
#   dict_time = t2.timeit(number=1000)

#   print("%d,%10.3f,%10.3f" % (i,list_time, dict_time))

def binarySearch(list, target):
  list.sort()
  left = list[0]
  right = len(list) - 1
  mid = 0

  while left <= right:
 
    mid = (right + left) // 2
 
    # If x is greater, ignore left half
    if list[mid] < target:
        left = mid + 1
 
    # If x is smaller, ignore right half
    elif list[mid] > target:
        right = mid - 1
        # return binarySearch()
 
    # means x is present at mid
    else:
      return mid
  
  return -1


def linearSearch(list, target):
  for i in range(0, len(list)):
    if(list[i] == target):
      return i
  return -1

print(binarySearch([ 2, 3, 4, 10, 40, 100, 12, 22,10 ], 22))
print(linearSearch([ 2, 3, 4, 10, 40, 100, 12, 22,10 ], 22))


