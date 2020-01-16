from pythonds.basic import Stack


class Calculator(object):
    def evaluate(self, string):
        return int(self.solve(self.infix_to_postfix(string)))
    def solve(self, postfix):
        operandStack = Stack()

        for token in postfix:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = self.doMath(token, operand1, operand2)
                operandStack.push(result)
        return operandStack.pop()

    def doMath(self, op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2

    def infix_to_postfix(self, string):
        precedence = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
        opStack = Stack()
        postfixList = []
        tokenList = string.split()

        for token in tokenList:
            if token in "0123456789":
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                        (precedence[opStack.peek()] >= precedence[token]):
                    postfixList.append(opStack.pop())
                opStack.push(token)

        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return postfixList


kap = Calculator().infix_to_postfix("2 / 2 + 3 * 4 - 6")
print(kap)
print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"))
