from pythonds.basic.queue import Queue
import random
# Assumptions
# 1. Customers queue at till to pay for goods
# 2. Till takes a second to scan goods
# 3. The more goods the more time spent at till
# 4. Cashier completes task once all goods are scanned and the customer pays
# 5. Shop is open for 13 hours in day
# 6. 

class Till:
  def __init__(self, speedOfScan) -> None:
    self.scanTime = speedOfScan
    self.timeRemaining = 0
    self.currentCustomer = None

  def tick(self):
    if self.currentCustomer != None:
      self.timeRemaining = self.timeRemaining - 1
      if self.timeRemaining <= 0:
        self.currentCustomer = None
  
  def busy(self):
    if self.currentCustomer != None:
      return True
    else:
      return False

  def serveNext(self, nextCustomer):
    self.currentCustomer = nextCustomer
    self.timeRemaining = nextCustomer.getNoOfItems() * self.scanTime


class Customer:
  def __init__(self, timestamp) -> None:
    self.timestamp = timestamp
    self.items = random.randrange(1, 101)

  def getNoOfItems(self):
    return self.items

  def waitTime(self,currentTime):
    return currentTime - self.timestamp


def simulation(numOfSeconds, scannerSpeed):
  till = Till(scannerSpeed)
  groceryQueue = Queue()
  waitingTime = []

  for currentSecond in range(numOfSeconds):
    if newWalkIn():
      newCustomer = Customer(currentSecond)
      groceryQueue.enqueue(newCustomer)

    if (not till.busy()) and (not groceryQueue.isEmpty()):
      # add waiting customer to the till and append to waitingTime how long they waited
      customer = groceryQueue.dequeue()
      till.serveNext(customer)
      waitingTime.append(customer.waitTime(currentSecond))
       
    till.tick()

  averageWaitTime = sum(waitingTime) / len(waitingTime)
  print("Average wait time: %6.2f seconds and number of customers remaining: %3d" %(averageWaitTime, groceryQueue.size()))

def newWalkIn():
  num = random.randrange(1, 157)
  if num == 156:
    return True
  else:
    return False

for i in range(10):
  simulation(46800, 2)