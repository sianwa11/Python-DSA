from pythonds.basic import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    try:
        tokenList = postfixExpr.split()

        for token in tokenList:
            if len(token) > 1:
                raise Exception('Fix the postfix expression to include spaces')

            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(token,operand1,operand2)
                operandStack.push(result)
        return operandStack.pop()
    except Exception as e:
        return 'Something wrong happened: ' + str(e)


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))
print(postfixEval('5 3 4 2 - ^ *'))