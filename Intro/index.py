
import random

goal = ''
# Function that generates string 28 characters long
def string_gen(strlen):
  alphabet = 'abcdefghijklmnopqrstuvwxyz '
  res = ""
  for i in range(strlen):
    res = res + alphabet[random.randrange(27)]
  return res


def score(goal,randstr):
  score = 0
  for i in range(len(goal)):
    if goal[i] == randstr[i]:
      score = score + 1
  return score / len(goal)


def repeat():

  goal = "methinks it is like a weasel"
  kwech = score(goal,string_gen(28))
  newString = string_gen(28)
  count = 0

  while(kwech < 1):
      newString = string_gen(28)
      count = count + 1

      if(newString == goal):
        print(newString)
        print(score(goal,string_gen(28)))
        print("We are done")
        break
      elif(count == 1000):
        print(newString)
        print(score(goal,string_gen(28)))
        # break
        count = 0
        
        

# print(score("methinks it is like a weasel",string_gen(28)))
repeat()
