from src.stack.StackArray import Stack


class PostfixCalculator:
    def calculate(self, *args):
        stack = Stack()
        operators = ['*', '/', '+', '-']
        for inputs in args:
            if type(inputs) is int:
                stack.push(inputs)
                continue
            r_value, l_value = stack.pop(), stack.pop()
            if inputs in operators:
                stack.push(eval('l_value {} r_value'.format(inputs)))

        return stack.pop()
