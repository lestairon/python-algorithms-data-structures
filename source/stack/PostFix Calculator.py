from Array import Stack

class PostfixCalculator:
  def calculate(self, *args):
    stack = Stack()
    for inputs in args:
      if type(inputs) is int:
        stack.push(inputs)
        continue
      r_value, l_value = stack.pop(), stack.pop()
      if inputs == '+':
        stack.push(l_value + r_value)
      elif inputs == '-':
        stack.push(l_value - r_value)
      elif inputs == '*':
        stack.push(l_value * r_value)
      elif inputs == '/':
        stack.push(l_value / r_value)

    return print(stack.pop())

s = PostfixCalculator()
s.calculate(5, 6, 7, '*', '+', 1, '-')