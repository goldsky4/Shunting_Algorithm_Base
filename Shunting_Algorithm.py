from Stack import Stack
from Queue import Queue

class Shunting_Algorithm:

    @staticmethod
    def precedence(op1, op2):
        precedences = {'+': 0, '-': 0, '*': 1, '/': 1, '^':2}
        return precedences[op1] > precedences[op2]

    @staticmethod
    def isnum(val):
        try:
            if int(val):
                return True
        except ValueError:
            return False

    @staticmethod
    def evaluate(exp):
        numbers = Stack()
        postfix = Shunting_Algorithm.postfix(exp)
        for i in postfix:

            if Shunting_Algorithm.isnum(i):
                numbers.push(i)
            else:
                right = int(numbers.pop())
                left = int(numbers.pop())

                if i == '+':
                    new = left+right
                elif i == '-':
                    new = left - right
                elif i == '*':
                    new = left * right
                elif i == '/':
                    new = left / right
                elif i == '^':
                    new = left ** right
                else:
                    return None
                numbers.push(new)
        return numbers.peek()


    @staticmethod
    def postfix(exp):
        output = Queue()
        operators = Stack()
        newexp = exp.split()
        for i in newexp:
            if Shunting_Algorithm.isnum(i):
                output.enqueue(i)
            elif i == '(':
                operators.push(i)
            elif i == ')':
                top = operators.peek()
                while top != '(' and not None:
                    output.enqueue(operators.pop())
                    top = operators.peek()
                operators.pop()
            else:
                top = operators.peek()
                while top != None and not '(' and Shunting_Algorithm.precedence(top, i):
                    output.enqueue(operators.pop())
                    top = operators.peek()

                operators.push(i)
        top = operators.peek()
        while top != None:
            output.enqueue(operators.pop())
            top = operators.peek()
        return output


exp = '( 53 + 3 ^ 2 ) + 3 * 4 / 4 '
print(Shunting_Algorithm.evaluate(exp))