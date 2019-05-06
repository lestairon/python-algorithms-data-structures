class Stack:

  def __init__(self):
    self.stack = []

  def push(self, new_data):
    self.stack.append(new_data)

  def pop(self):
    if len(self.stack) <= 0:
      raise IndexError('Stack is already empty')
    else:
      return self.stack.pop()

  def count(self):
    return len(self.stack)

  def peek(self):
    if len(self.stack) <= 0:
      raise IndexError('List is Empty')
    else:
      return self.stack[-1]

  def clear(self):
    del self.stack[:]

  def enumerate(self):
    return print(*self.stack[::-1], sep=', ')