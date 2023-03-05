def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

def lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def comparison(x, y):
     common = lcm(x.den, y.den)
     num1 = (x.num * common) / x.den
     num2 = (y.num * common) / y.den

     return {"num1": num1, "num2": num2}


class Fraction:
     def __init__(self,top,bottom):
        try:
         common = gcd(top,bottom)
         self.num = top // common
         self.den = bottom // common

         if isinstance(self.num, int) == False or isinstance(self.den, int) == False:
          raise
        except:
          print("Only integers allowed")
          exit()

     def getNum(self):
        return self.num

     def getDen(self):
        return self.den

     def __gt__(self, other):
        compare = comparison(self, other)
        num1 = compare["num1"]
        num2 = compare["num2"]

        if num1 > num2 :
          print("True")
        else:
          print("False")
        return

     def __ge__(self,other):
        compare = comparison(self, other)
        num1 = compare["num1"]
        num2 = compare["num2"]

        if num1 >= num2 :
          print("True")
        else:
          print("False")
        return

     def __lt__(self,other):
        compare = comparison(self, other)
        num1 = compare["num1"]
        num2 = compare["num2"]

        if num1 < num2 :
          print("True")
        else:
          print("False")
        return

     def __le__(self,other):
        compare = comparison(self, other)
        num1 = compare["num1"]
        num2 = compare["num2"]

        if num1 <= num2 :
          print("True")
        else:
          print("False")
        return


     def __ne__(self,other):
        compare = comparison(self, other)
        num1 = compare["num1"]
        num2 = compare["num2"]

        if num1 != num2 :
          print("True")
        else:
          print("False")
        return
      

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
        #  common = gcd(newnum,newden)
        #  return Fraction(newnum//common,newden//common)
         return Fraction(newnum, newden)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

     def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

     def __truediv__(self, other):
        othernum = other.den
        otherden = other.num

        newnum = self.num * othernum
        newden = self.den * otherden


        return Fraction(newnum, newden)

     def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)


x = Fraction(5,12)
y = Fraction(5,12)

x.__ge__(y)


