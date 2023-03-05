# from pythonds.basic import Stack
from stack import Stack


# Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion and the postfix evaluation algorithm. Your evaluator should process infix tokens from left to right and use two stacks, one for operators and one for operands, to perform the evaluation.
def infixEvaluator(expression):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    operatorStack = Stack()
    operandStack = Stack()
    postfixList = []

    try:
        tokenList = expression.split()

        for token in tokenList:
            # if len(token) > 1:
            #     raise Exception('Fix the infix expression to include spaces')

            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfixList.append(token)
            elif token == '(':
                operatorStack.push(token)
            elif token == ')':
                topToken = operatorStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = operatorStack.pop()
            else:
                while (not operatorStack.isEmpty()) and (prec[operatorStack.peek()] >= prec[token]):
                    postfixList.append(operatorStack.pop())

                operatorStack.push(token)

        while not operatorStack.isEmpty():
            postfixList.append(operatorStack.pop())

        postfixExpression = " ".join(postfixList).split()

        for token in postfixExpression:
          if token in '0123456789':
            operandStack.push(int(token))
          else:
            operator2 = operandStack.pop()
            operator1 = operandStack.pop()
            result = doMath(token, operator1, operator2)
            operandStack.push(result)

        return {
          "postfix" : " ".join(postfixList),
          "postfix evaluation" : operandStack.pop()
          }

    except Exception as e:
        return 'Something wrong happened: ' + str(e)


def doMath(operator, op1, op2):
  if operator == "*":
    return op1 * op2
  elif operator == "/":
    return op1 / op2
  elif operator == "+":
    return op1 + op2
  else:
    return op1 - op2

# print(infixEvaluator("( A + B ) * C - ( D - E ) * ( F + G )"))
# print(infixEvaluator("5 * 3 ^ ( 4 - 2 )"))
# print(infixEvaluator("( 9 * 3 ) / ( 6 - 3 )"))


# Turn your direct infix evaluator from the previous problem into a calculator.
def calculator():
  try:
    print('---KEY IN YOUR Expression---')
    print('only accepts (0-9),(*,/,+,-) and ()')
    expresion = input()
    finalList = list()
    expressionString = ''

    for exp in list(expresion):
      if exp in '0123456789':
        expressionString = expressionString + exp
      else:
        if expressionString != '':
          finalList.append(expressionString)
        finalList.append(exp)
        expressionString = ''
    
    if len(expressionString) > 0:
      finalList.append(expressionString)
    
    return infixEvaluator(" ".join(finalList))
  except Exception as e:
    return 'Error: '+ str(e)

print(calculator())
