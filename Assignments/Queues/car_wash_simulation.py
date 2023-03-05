# Cars lined up at a car wash

from pythonds.basic.queue import Queue
import random

class Car:
  # 7200 - Handwashed carwash
  # 240 -Touchless carwash
  # 300 - auto carwash
  def __init__(self, time):
    self.timestamp = time
    self.steps = random.choice([4,5])
  
  def getStamp(self):
    return self.timestamp

  def getT(self):
    return self.steps

  def waitTime(self, currenttime):
    return currenttime - self.timestamp



class CarWash:
  def __init__(self,stepsperminute) -> None:
    # factors affecting speed of car wash include equipment,no of steps & time for each step
    self.washRate = stepsperminute
    self.currentCar = None
    self.timeRemaining = 0

  def tick(self):
    if self.currentCar != None:
      self.timeRemaining = self.timeRemaining - 1
      if self.timeRemaining <= 0:
          self.currentCar = None
  
  def isBusy(self):
    if self.currentCar != None:
      return True
    else:
      return False

  def washNext(self, nextCar):
    self.currentCar = nextCar
    self.timeRemaining = nextCar.getT() + self.washRate



def simulation(numSeconds, stepsPerMinute):
    carWash = CarWash(stepsPerMinute)
    carQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         car = Car(currentSecond)
         carQueue.enqueue(car)

      if (not carWash.isBusy()) and (not carQueue.isEmpty()):
        nextCar = carQueue.dequeue()
        waitingtimes.append(nextCar.waitTime(currentSecond))
        carWash.washNext(nextCar)

      carWash.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f minutes %3d cars remaining."%(averageWait,carQueue.size()))

def newPrintTask():
    num = random.randrange(1,61)
    if num == 60:
        return True
    else:
        return False

for i in range(10):
    simulation(1440,10)