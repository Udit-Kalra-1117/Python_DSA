def checkIfOperand(c):
    return c.isalpha()

def checkPrecedence(ch, stack_top):
    precedence = {'+':1, '-':1, '/':2, '*':2, '^':3}

    try:
        a = precedence[ch]
        b = precedence[stack_top]

        return True if a <= b else False
    except KeyError:
        return False

def convertInfixToPostfix(exp):
    stack = []
    result = []

    for i in range(len(exp)):
        if checkIfOperand(exp[i]):
            result.append(exp[i])
        elif exp[i] == '(':
            stack.append(exp[i])
        elif exp[i] == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result.append(stack.pop())
            if len(stack) > 0 and stack[-1] != '(':
                return # invalid expression case
            else:
                stack.pop()
        else:
            while len(stack) > 0 and checkPrecedence(exp[i], stack[-1]):
                result.append(stack.pop())

            stack.append(exp[i])
    while len(stack) > 0:
        result.append(stack.pop())
    
    return result

def convertInfixToPrefix(expr):
    list = [x for x in expr]
    list.reverse()

    for i in range(len(list)):
        if list[i] == '(':
            list[i] = ")"
        elif list[i] == ')':
            list[i] = "("

    result = convertInfixToPostfix(list)
    result.reverse()

    print("".join(x for x in result))

# Driver Code
expression = "a+b*(c^d-e)^(f+g*h)-i"
print()
convertInfixToPrefix(expression)
print()
