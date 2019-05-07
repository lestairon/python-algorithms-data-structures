class QueueArray:

  def __init__(self):
    self.queue = []

  def enqueue(self, new_data):
    self.queue.append(new_data)

  def dequeue(self):
    if len(self.queue) <= 0:
      raise IndexError('Queue is already empty')
    else:
      return self.queue.pop(0)

  def count(self):
    return len(self.queue)

  def peek(self):
    if len(self.queue) <= 0:
      raise IndexError('List is Empty')
    else:
      return self.queue[0]

  def clear(self):
    del self.queue[:]

  def enumerate(self):
    return print(*self.queue, sep=', ')